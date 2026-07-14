"""Tests for the tax module (src/tax.py)."""

import pytest
from src.tax import (
    DealTaxProfile,
    TaxConfig,
    build_deal_tax_profile,
    compute_annual_depreciation,
    compute_scenario_tax,
    run_tax_analysis,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def default_config() -> TaxConfig:
    return TaxConfig()


@pytest.fixture
def sandpainter_config() -> TaxConfig:
    return TaxConfig(
        marginal_federal_rate=0.37,
        lp_type="ideal",
        land_ratio=0.20,
        residential_years=27.5,
        cost_segregation_pct=0.25,
        bonus_depreciation_rate=1.00,
        interest_deductible=True,
    )


# ---------------------------------------------------------------------------
# DealTaxProfile
# ---------------------------------------------------------------------------

class TestDealTaxProfile:
    def test_basic_residential(self, sandpainter_config):
        profile = build_deal_tax_profile(
            "test_deal", 23_000_000, 16_000_000, 0.075, sandpainter_config, True
        )
        # Building basis = 23M * 0.80 = 18.4M
        assert profile.building_basis == pytest.approx(18_400_000)
        # Cost seg = 18.4M * 0.25 = 4.6M
        assert profile.cost_seg_basis == pytest.approx(4_600_000)
        # Remaining = 18.4M - 4.6M = 13.8M
        assert profile.remaining_building_basis == pytest.approx(13_800_000)
        # Bonus Y1 = 4.6M * 1.0 = 4.6M
        assert profile.bonus_depreciation_y1 == pytest.approx(4_600_000)
        # SL = 13.8M / 27.5 = 501,818...
        assert profile.annual_sl_depreciation == pytest.approx(13_800_000 / 27.5)
        assert profile.recovery_years == 27.5

    def test_interest_deduction(self, sandpainter_config):
        profile = build_deal_tax_profile(
            "test", 23_000_000, 16_000_000, 0.075, sandpainter_config, True
        )
        assert profile.debt_balance == 16_000_000
        assert profile.interest_rate == 0.075

    def test_commercial_property(self, sandpainter_config):
        profile = build_deal_tax_profile(
            "commercial", 50_000_000, 30_000_000, 0.06, sandpainter_config, False
        )
        assert profile.recovery_years == 39.0
        # Building basis = 50M * 0.8 = 40M
        assert profile.building_basis == pytest.approx(40_000_000)


# ---------------------------------------------------------------------------
# Annual depreciation
# ---------------------------------------------------------------------------

class TestAnnualDepreciation:
    def test_year1_bonus(self, sandpainter_config):
        profile = build_deal_tax_profile(
            "test", 23_000_000, 16_000_000, 0.075, sandpainter_config, True
        )
        bonus, sl = compute_annual_depreciation(profile, 1, sandpainter_config)
        assert bonus == pytest.approx(4_600_000)
        assert sl == pytest.approx(13_800_000 / 27.5)

    def test_year2_no_bonus(self, sandpainter_config):
        profile = build_deal_tax_profile(
            "test", 23_000_000, 16_000_000, 0.075, sandpainter_config, True
        )
        bonus, sl = compute_annual_depreciation(profile, 2, sandpainter_config)
        assert bonus == 0.0
        assert sl == pytest.approx(13_800_000 / 27.5)

    def test_year30_no_sl(self, sandpainter_config):
        """After 27.5 years, straight-line depreciation ends."""
        profile = build_deal_tax_profile(
            "test", 23_000_000, 16_000_000, 0.075, sandpainter_config, True
        )
        bonus, sl = compute_annual_depreciation(profile, 30, sandpainter_config)
        assert bonus == 0.0
        assert sl == 0.0

    def test_mid_life(self, sandpainter_config):
        """Year 10 should have SL but no bonus."""
        profile = build_deal_tax_profile(
            "test", 23_000_000, 16_000_000, 0.075, sandpainter_config, True
        )
        bonus, sl = compute_annual_depreciation(profile, 10, sandpainter_config)
        assert bonus == 0.0
        assert sl == pytest.approx(13_800_000 / 27.5)


# ---------------------------------------------------------------------------
# Scenario tax computation
# ---------------------------------------------------------------------------

class TestComputeScenarioTax:
    def _make_yearly(self, year, noi=2_000_000, hf_gain=500_000,
                     hf_reinvest_re=0, hf_reinvest_hf=0,
                     lp_dist=1_000_000):
        return {
            "year": year,
            "re_noi": noi,
            "hf_harvest_generated": hf_gain,
            "hf_reinvestment_source_re": hf_reinvest_re,
            "hf_reinvestment_source_hf": hf_reinvest_hf,
            "lp_distribution": lp_dist,
            "lp_cash_distributions": lp_dist,
            "hf_opening_nav": 800_000,
            "hf_closing_nav": 800_000 * 1.1,
            "hf_return": 0.10,
        }

    def test_basic_shield(self, sandpainter_config):
        """Tax savings should be positive when depreciation > 0."""
        profile = build_deal_tax_profile(
            "jon_deal_1", 23_000_000, 16_000_000, 0.075, sandpainter_config, True
        )
        yearly = [self._make_yearly(y, noi=2_000_000, hf_gain=500_000) for y in range(1, 6)]
        result = compute_scenario_tax(
            "test", "Test", yearly, [profile], sandpainter_config, 10_000_000
        )
        # Year 1 should have large bonus depreciation + interest
        y1 = result.yearly[0]
        assert y1.bonus_depreciation == pytest.approx(4_600_000)
        assert y1.interest_deduction == pytest.approx(1_200_000)  # 16M * 0.075
        assert y1.tax_savings > 0

    def test_after_tax_moic_improves(self, sandpainter_config):
        """After-tax MOIC should be >= pre-tax MOIC."""
        profile = build_deal_tax_profile(
            "jon_deal_1", 23_000_000, 16_000_000, 0.075, sandpainter_config, True
        )
        yearly = [self._make_yearly(y, noi=2_000_000, hf_gain=500_000, lp_dist=1_000_000) for y in range(1, 11)]
        result = compute_scenario_tax(
            "test", "Test", yearly, [profile], sandpainter_config, 10_000_000
        )
        # After-tax MOIC should be higher due to tax savings on $10M capital
        pre_tax_moic = sum(y["lp_distribution"] for y in yearly) / 10_000_000
        assert result.final_after_tax_moic >= pre_tax_moic

    def test_no_tax_benefit_without_depreciation(self, default_config):
        """Without real estate (no deals), tax savings should be zero."""
        yearly = [self._make_yearly(y, noi=0, hf_gain=500_000) for y in range(1, 6)]
        result = compute_scenario_tax(
            "test", "Test", yearly, [], default_config, 10_000_000
        )
        assert result.total_tax_savings == 0.0

    def test_cumulative_depreciation(self, sandpainter_config):
        """Cumulative depreciation should increase each year."""
        profile = build_deal_tax_profile(
            "jon_deal_1", 23_000_000, 16_000_000, 0.075, sandpainter_config, True
        )
        yearly = [self._make_yearly(y) for y in range(1, 6)]
        result = compute_scenario_tax(
            "test", "Test", yearly, [profile], sandpainter_config, 10_000_000
        )
        cum_deps = [yt.cumulative_depreciation for yt in result.yearly]
        for i in range(1, len(cum_deps)):
            assert cum_deps[i] > cum_deps[i - 1]

    def test_hf_stcg_calculation(self, sandpainter_config):
        """HF STCG should include harvest + reinvested amounts."""
        profile = build_deal_tax_profile(
            "jon_deal_1", 23_000_000, 16_000_000, 0.075, sandpainter_config, True
        )
        yearly = [self._make_yearly(1, hf_gain=500_000, hf_reinvest_re=200_000, hf_reinvest_hf=100_000)]
        result = compute_scenario_tax(
            "test", "Test", yearly, [profile], sandpainter_config, 10_000_000
        )
        assert result.yearly[0].hf_stcg == pytest.approx(700_000)

    def test_ideal_lp_uses_passive_losses_against_portfolio(self, sandpainter_config):
        """Ideal LP should be able to use passive losses to offset HF gains."""
        profile = build_deal_tax_profile(
            "jon_deal_1", 23_000_000, 16_000_000, 0.075, sandpainter_config, True
        )
        # Large HF gain, small NOI → passive loss should offset HF gain
        yearly = [self._make_yearly(1, noi=500_000, hf_gain=2_000_000)]
        result = compute_scenario_tax(
            "test", "Test", yearly, [profile], sandpainter_config, 10_000_000
        )
        y1 = result.yearly[0]
        savings = y1.tax_savings
        assert savings > 0
        # Tax savings should be meaningful — depreciation is huge in Y1
        # Total deductions = 4.6M bonus + 502K SL + 1.2M interest = 6.3M
        # Taxable income no benefit = 2M + 0.5M - 1.2M = 1.3M
        # Taxable income with benefit = 2M - 6.3M = -4.3M → 0
        # Tax savings = 1.3M * 0.37 = 481K
        assert savings == pytest.approx(1_300_000 * 0.37, rel=0.01)

    def test_passive_loss_carryforward(self, sandpainter_config):
        """Unused passive losses should carry forward."""
        profile = build_deal_tax_profile(
            "jon_deal_1", 23_000_000, 16_000_000, 0.075, sandpainter_config, True
        )
        # No HF gains → passive losses can't be used, should carry forward
        yearly = [self._make_yearly(y, hf_gain=0, noi=500_000) for y in range(1, 4)]
        result = compute_scenario_tax(
            "test", "Test", yearly, [profile], sandpainter_config, 10_000_000
        )
        # Passive loss carryforward should grow
        final_cf = result.yearly[-1].passive_loss_carryforward
        assert final_cf > 0

    def test_config_from_defaults(self):
        config = TaxConfig()
        assert config.marginal_federal_rate == 0.37
        assert config.lp_type == "ideal"
        assert config.land_ratio == 0.20
        assert config.cost_segregation_pct == 0.25
        assert config.bonus_depreciation_rate == 1.00

    def test_irr_computation(self, sandpainter_config):
        """After-tax IRR should be computable for a realistic scenario."""
        profile = build_deal_tax_profile(
            "jon_deal_1", 23_000_000, 16_000_000, 0.075, sandpainter_config, True
        )
        # 20 years of cash flows with growing distributions
        yearly = []
        for y in range(1, 21):
            dist = 500_000 + y * 100_000  # growing from 600K to 2.5M
            yearly.append(self._make_yearly(y, noi=2_000_000, hf_gain=400_000, lp_dist=dist))
        result = compute_scenario_tax(
            "test", "Test", yearly, [profile], sandpainter_config, 10_000_000
        )
        assert result.final_after_tax_irr is not None
        assert result.final_after_tax_irr > 0
