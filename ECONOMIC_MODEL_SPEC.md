# Economic Model Spec

The authoritative design specification for this phase 1 build is the workspace-level `economic_model_spec.md` supplied with the project prompt.

This implementation follows the requested version 1 scope:

- annual deterministic scenario engine
- YAML-driven assumptions
- real estate, hedge fund, reserve, LP waterfall, GP fees, GP residual value
- CSV, Excel, and Markdown outputs
- pytest coverage for metrics, waterfall, and basic engine behavior

Excluded from phase 1:

- frontend
- database
- Monte Carlo
- tax modelling
- detailed debt or property-level modelling
- monthly periods
