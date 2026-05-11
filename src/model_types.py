from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

from pydantic import BaseModel, Field, ValidationError, field_validator, model_validator


AllocationMethod = Literal["fixed", "cap_rate_sized"]
FeeBasis = Literal["gross_rent", "noi", "re_nav"]
CashYieldSource = Literal["net_re_cashflow", "hf_harvest", "retained_cash", "reserve"]
RefinanceUseOfProceeds = Literal["lp_distribution", "retained_cash", "reserve"]


class ModelSettings(BaseModel):
    currency: str = "USD"
    periods_per_year: int = 1
    max_years: int = Field(gt=0)
    initial_lp_capital: float = Field(gt=0)
    gp_co_investment: float = Field(default=0, ge=0)

    @field_validator("periods_per_year")
    @classmethod
    def annual_only(cls, value: int) -> int:
        if value != 1:
            raise ValueError("Version 1 supports annual periods only: periods_per_year must be 1.")
        return value


class AllocationSettings(BaseModel):
    method: AllocationMethod
    hedge_fund_allocation_pct: float = Field(ge=0)
    real_estate_allocation_pct: float = Field(ge=0)
    reserve_allocation_pct: float = Field(ge=0)


class WaterfallSettings(BaseModel):
    lp_hurdle_moic: float = Field(gt=0)
    lp_receives_100_percent_until_hurdle: bool = True
    gp_receives_residual_after_lp_hurdle: bool = True
    include_unrealized_nav_in_hurdle_test: bool = True
    require_liquidity_for_lp_redemption: bool = True


class LiquiditySettings(BaseModel):
    hf_liquidation_allowed: bool = True
    hf_liquidation_capacity_pct_per_year: float = Field(ge=0, le=1)
    reserve_liquidation_capacity_pct_per_year: float = Field(ge=0, le=1)
    real_estate_liquidation_capacity_pct_per_year: float = Field(default=0, ge=0, le=1)
    max_refinance_or_sale_capacity_pct_of_re_nav: float = Field(ge=0, le=1)


class RealEstateAssetManagementFee(BaseModel):
    enabled: bool = True
    rate: float = Field(ge=0)
    basis: FeeBasis = "gross_rent"


class HedgeFundFees(BaseModel):
    model_as_net_returns: bool = True
    management_fee_rate: float = Field(default=0, ge=0)
    performance_fee_rate: float = Field(default=0, ge=0)


class FeeSettings(BaseModel):
    real_estate_asset_management_fee: RealEstateAssetManagementFee
    hedge_fund_fees: HedgeFundFees


class DistributionPolicy(BaseModel):
    distribute_re_cashflow_annually: bool = True
    distribute_hf_realized_gains_annually: bool = False
    hf_positive_return_harvest_rate: float = Field(default=0, ge=0, le=1)
    retain_cash_until_hurdle_redemption: bool = False


class LPCashYieldPolicy(BaseModel):
    enabled: bool = False
    target_annual_yield_on_unreturned_capital: float = Field(default=0.0, ge=0)
    source_priority: list[CashYieldSource] = Field(
        default_factory=lambda: ["net_re_cashflow", "hf_harvest", "retained_cash", "reserve"]
    )
    reduce_lp_hurdle: bool = True

    @field_validator("source_priority")
    @classmethod
    def source_priority_required(cls, value: list[CashYieldSource]) -> list[CashYieldSource]:
        if not value:
            raise ValueError("LP cash yield source_priority must contain at least one source.")
        return value


class ReserveSettings(BaseModel):
    annual_return: float = 0


class ReportingSettings(BaseModel):
    output_excel: bool = True
    output_csv: bool = True
    output_markdown: bool = True


class FlagThresholds(BaseModel):
    fast_gp_dynasty_max_year: int = Field(default=4, gt=0)
    fast_gp_dynasty_residual_multiple: float = Field(default=0.5, ge=0)
    slow_time_horizon_year: int = Field(default=8, gt=0)
    gp_survivability_first_years: int = Field(default=5, gt=0)
    gp_survivability_fee_threshold: float = Field(default=250_000, ge=0)
    hf_major_drawdown_pct: float = Field(default=0.50, ge=0, le=1)
    re_nav_impairment_pct: float = Field(default=0.20, ge=0, le=1)
    lp_good_irr_threshold: float = Field(default=0.12)
    lp_good_irr_gp_residual_multiple: float = Field(default=1.0, ge=0)
    long_zero_distribution_years: int = Field(default=3, gt=0)


class GPSurvivabilitySettings(BaseModel):
    first_n_years: int = Field(default=5, gt=0)
    minimum_cumulative_fees: float = Field(default=500_000, ge=0)
    minimum_average_annual_fees: float = Field(default=100_000, ge=0)


class ModelConfig(BaseModel):
    model: ModelSettings
    allocation: AllocationSettings
    waterfall: WaterfallSettings
    liquidity: LiquiditySettings
    fees: FeeSettings
    distribution_policy: DistributionPolicy
    lp_cash_yield_policy: LPCashYieldPolicy = LPCashYieldPolicy()
    reserve: ReserveSettings = ReserveSettings()
    reporting: ReportingSettings
    flag_thresholds: FlagThresholds
    gp_survivability: GPSurvivabilitySettings = GPSurvivabilitySettings()

    @model_validator(mode="after")
    def validate_allocation(self) -> "ModelConfig":
        if self.allocation.method == "fixed":
            total = (
                self.allocation.hedge_fund_allocation_pct
                + self.allocation.real_estate_allocation_pct
                + self.allocation.reserve_allocation_pct
            )
            if abs(total - 1.0) > 1e-6:
                raise ValueError("Fixed allocation percentages must sum to 1.0.")
        return self


class RealEstateScenario(BaseModel):
    initial_noi_yield: float
    annual_noi_growth: float
    annual_nav_appreciation: float | list[float]
    gross_rent_yield: float | list[float]


class HedgeFundScenario(BaseModel):
    annual_returns: list[float]

    @field_validator("annual_returns")
    @classmethod
    def returns_required(cls, value: list[float]) -> list[float]:
        if not value:
            raise ValueError("Each scenario must provide at least one hedge fund return.")
        return value


class RefinanceEvent(BaseModel):
    year: int = Field(gt=0)
    pct_of_re_nav: float = Field(ge=0)
    use_of_proceeds: RefinanceUseOfProceeds
    description: str = ""


class Scenario(BaseModel):
    description: str
    years: int = Field(gt=0)
    real_estate: RealEstateScenario
    hedge_fund: HedgeFundScenario
    liquidity: dict[str, Any] | None = None
    distribution_policy: dict[str, Any] | None = None
    lp_cash_yield_policy: dict[str, Any] | None = None
    allocation: dict[str, Any] | None = None
    reserve: dict[str, Any] | None = None
    refinance_events: list[RefinanceEvent] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_years(self) -> "Scenario":
        if len(self.hedge_fund.annual_returns) < self.years:
            raise ValueError(
                f"Scenario requires {self.years} hedge fund returns but only "
                f"{len(self.hedge_fund.annual_returns)} were provided."
            )
        for event in self.refinance_events:
            if event.year > self.years:
                raise ValueError(f"Refinance event year {event.year} exceeds scenario years {self.years}.")
        return self


class ScenarioSet(BaseModel):
    scenarios: dict[str, Scenario]

    @field_validator("scenarios")
    @classmethod
    def non_empty(cls, value: dict[str, Scenario]) -> dict[str, Scenario]:
        if not value:
            raise ValueError("scenarios.yaml must contain at least one scenario.")
        return value


@dataclass
class YearlyResult:
    scenario: str
    year: int
    re_opening_nav: float
    re_noi_yield: float
    re_noi: float
    gross_rent: float
    re_asset_mgmt_fee: float
    net_re_cashflow: float
    re_appreciation_rate: float
    re_closing_nav: float
    hf_opening_nav: float
    hf_return: float
    hf_harvest: float
    hf_closing_nav: float
    refinance_proceeds: float
    refinance_use_of_proceeds: str
    cumulative_refinance_proceeds: float
    reserve_opening_nav: float
    reserve_closing_nav: float
    retained_cash: float
    lp_cash_yield_target: float
    lp_cash_yield_paid: float
    lp_cash_yield_shortfall: float
    cumulative_lp_cash_yield_shortfall: float
    lp_cash_yield_coverage_ratio: float | None
    lp_distribution: float
    lp_cumulative_distribution: float
    lp_remaining_hurdle: float
    economic_hurdle_passed: bool
    liquidity_available: float
    liquidity_hurdle_passed: bool
    gp_fees: float
    gp_cumulative_fees: float
    gp_residual_nav: float
    fund_nav: float
    event_flag: str = ""


@dataclass
class FlagResult:
    scenario: str
    flag: str
    severity: str
    explanation: str


@dataclass
class ScenarioResult:
    scenario: str
    description: str
    summary: dict[str, Any]
    cashflows: list[YearlyResult] = field(default_factory=list)
    flags: list[FlagResult] = field(default_factory=list)


def pydantic_error_message(path: str, exc: ValidationError) -> str:
    return f"Invalid assumptions in {path}: {exc}"
