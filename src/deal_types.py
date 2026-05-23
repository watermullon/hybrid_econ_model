from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from pydantic import BaseModel, Field, field_validator, model_validator


ValueType = Literal["unknown", "current", "appraised", "stabilized", "replacement", "purchase_price"]
AmortizationType = Literal["interest_only", "fixed_annual_debt_service"]
ValuationMethod = Literal["growth", "cap_rate", "fixed_stabilized_value"]
RefiProceedsUse = Literal["fund_liquidity", "retained_cash", "reserve"]


class DealAcquisition(BaseModel):
    asset_value: float = Field(gt=0)
    value_type: ValueType = "unknown"
    purchase_price: float | None = Field(default=None, ge=0)
    new_equity_required: float = Field(ge=0)
    closing_costs: float = Field(default=0, ge=0)
    initial_capex_reserve: float = Field(default=0, ge=0)


class DealCapitalStack(BaseModel):
    assumed_debt: float = Field(default=0, ge=0)
    assumed_liabilities: float = Field(default=0, ge=0)
    liabilities_written_down: float = Field(default=0, ge=0)
    seller_note: float = Field(default=0, ge=0)
    preferred_equity: float = Field(default=0, ge=0)


class DealOperations(BaseModel):
    current_noi: float | None = None
    stabilized_noi: float | None = None
    years_to_stabilization: int = Field(default=3, ge=0)
    annual_noi_growth_after_stabilization: float = 0.0
    gross_rent: float | None = Field(default=None, ge=0)
    gross_rent_growth: float = 0.0
    vacancy_rate: float | None = Field(default=None, ge=0, le=1)


class DealDebt(BaseModel):
    interest_rate: float | None = Field(default=None, ge=0)
    maturity_year: int | None = Field(default=None, gt=0)
    amortization_type: AmortizationType = "interest_only"
    annual_debt_service: float | None = Field(default=None, ge=0)
    amortization_years: int | None = Field(default=None, gt=0)
    dscr_minimum: float | None = Field(default=None, ge=0)
    recourse: str = "unknown"


class DealCapex(BaseModel):
    annual_capex: dict[int, float] = Field(default_factory=dict)
    recurring_capex_pct_of_noi: float = Field(default=0, ge=0)

    @field_validator("annual_capex")
    @classmethod
    def validate_capex_years(cls, value: dict[int, float]) -> dict[int, float]:
        for year, amount in value.items():
            if year <= 0:
                raise ValueError("Capex years must be positive integers.")
            if amount < 0:
                raise ValueError("Capex amounts must be non-negative.")
        return value


class DealValuation(BaseModel):
    method: ValuationMethod = "growth"
    exit_cap_rate: float | None = Field(default=None, gt=0)
    annual_value_growth: float = 0.0
    stabilized_value: float | None = Field(default=None, ge=0)


class DealRefinance(BaseModel):
    enabled: bool = True
    target_years: list[int] = Field(default_factory=list)
    refi_ltv: float = Field(default=0.65, ge=0, le=1)
    refi_costs_pct: float = Field(default=0.02, ge=0, le=1)
    max_cash_out_pct_of_value: float | None = Field(default=None, ge=0, le=1)
    proceeds_use: RefiProceedsUse = "fund_liquidity"

    @field_validator("target_years")
    @classmethod
    def target_years_must_be_positive(cls, value: list[int]) -> list[int]:
        if any(year <= 0 for year in value):
            raise ValueError("Refinance target years must be positive.")
        return sorted(set(value))


class DealConfig(BaseModel):
    enabled: bool = True
    acquisition_year: int = Field(gt=0)
    description: str = ""
    acquisition: DealAcquisition
    capital_stack: DealCapitalStack
    operations: DealOperations
    debt: DealDebt
    capex: DealCapex = DealCapex()
    valuation: DealValuation = DealValuation()
    refinance: DealRefinance = DealRefinance()

    @model_validator(mode="after")
    def validate_deal(self) -> "DealConfig":
        if self.operations.current_noi is None and self.operations.stabilized_noi is None:
            raise ValueError("Deal requires at least current_noi or stabilized_noi.")
        if self.debt.amortization_type == "interest_only" and self.debt.interest_rate is None:
            raise ValueError("interest_only debt requires interest_rate.")
        if self.debt.amortization_type == "fixed_annual_debt_service" and self.debt.annual_debt_service is None:
            raise ValueError("fixed_annual_debt_service requires annual_debt_service.")
        if self.valuation.method == "cap_rate" and self.valuation.exit_cap_rate is None:
            raise ValueError("cap_rate valuation requires exit_cap_rate.")
        if self.valuation.method == "fixed_stabilized_value" and self.valuation.stabilized_value is None:
            raise ValueError("fixed_stabilized_value valuation requires stabilized_value.")
        return self


class DealSet(BaseModel):
    deals: dict[str, DealConfig]

    @field_validator("deals")
    @classmethod
    def deals_required(cls, value: dict[str, DealConfig]) -> dict[str, DealConfig]:
        if not value:
            raise ValueError("deals.yaml must contain at least one deal.")
        return value


@dataclass
class DealYearResult:
    scenario: str
    deal_name: str
    year: int
    relative_year: int | None
    active: bool
    asset_value: float
    debt_balance: float
    assumed_liabilities: float
    net_equity_value: float
    noi: float
    gross_rent: float
    debt_service: float
    capex: float
    free_cashflow_after_debt_and_capex: float
    dscr: float | None
    prior_refi_liability: float
    ending_refi_liability: float
    max_debt_supported: float
    cash_out_before_refi_costs: float
    refi_costs: float
    refi_capacity: float
    refi_proceeds: float
    refi_liability_added: float
    deal_nav_before_refi_liability: float
    deal_nav_after_refi_liability: float
    deal_nav: float
    entry_equity_cushion: float
    value_to_new_equity_multiple: float | None
    new_equity_required: float
    refinance_proceeds_use: str


@dataclass
class RealEstatePortfolioYearResult:
    scenario: str
    year: int
    active_deal_count: int
    gross_asset_value: float
    debt_balance: float
    assumed_liabilities: float
    net_equity_value: float
    noi: float
    gross_rent: float
    debt_service: float
    capex: float
    free_cashflow_after_debt_and_capex: float
    dscr: float | None
    prior_refi_liability: float
    ending_refi_liability: float
    max_debt_supported: float
    cash_out_before_refi_costs: float
    refi_costs: float
    refi_capacity: float
    refi_proceeds: float
    refinance_liability_added: float
    deal_nav_before_refi_liability: float
    deal_nav_after_refi_liability: float
    deal_nav: float
    entry_equity_cushion: float
    value_to_new_equity_multiple: float | None
