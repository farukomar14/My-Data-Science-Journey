import json

data = {
    "company": "Air France-KLM Group",
    "report_type": "Annual Results 2025",
    "publication_date": "2026-02-19",
    "language": "French (extracted and translated to English)",

    "key_highlights": {
        "revenue_billion_eur": 33.0,
        "revenue_growth_pct": 4.9,
        "operating_result_billion_eur": 2.0,
        "operating_result_improvement_billion_eur": 0.4,
        "operating_margin_pct": 6.1,
        "operating_margin_improvement_pts": 1.0,
        "unit_revenue_growth_constant_fx_pct": 1.0,
        "unit_cost_increase_pct": 1.2,
        "fuel_price_decrease_pct": 7.0,
        "group_capacity_growth_pct": 4.9,
        "next_gen_fleet_share_pct": 35,
        "next_gen_fleet_growth_pts": 8,
        "liquidity_billion_eur": 9.4,
        "net_debt_ebitda_ratio": 1.7,
        "adjusted_recurring_free_operating_cashflow_billion_eur": 1.0,
        "adjusted_recurring_free_operating_cashflow_growth_billion_eur": 0.8,
        "sas_stake_target_pct": 60.5
    },

    "q4_2025_highlights": {
        "unit_revenue_change_constant_fx_pct": -0.5,
        "unit_cost_change_pct": -1.1,
        "operating_result_million_eur": 393,
        "operating_result_vs_prior_year_million_eur": "stable"
    },

    "full_year_2025_financials": {
        "passengers_thousands": 102844,
        "passengers_growth_pct": 5.0,
        "capacity_million_sko": 336521,
        "capacity_growth_pct": 4.9,
        "traffic_million_pkt": 293485,
        "traffic_growth_pct": 4.3,
        "load_factor_pct": 87.2,
        "load_factor_change_pts": -0.5,
        "revenue_million_eur": 33007,
        "revenue_growth_pct": 4.9,
        "revenue_growth_constant_fx_pct": 6.2,
        "operating_result_million_eur": 2004,
        "operating_result_change_million_eur": 403,
        "operating_margin_pct": 6.1,
        "operating_margin_change_pts": 1.0,
        "net_result_million_eur": 1754,
        "net_result_change_million_eur": 1265,
        "unit_revenue_per_sko_cents": 8.80,
        "unit_revenue_change_pct": -0.2,
        "unit_revenue_change_constant_fx_pct": 1.0,
        "unit_cost_per_sko_cents": 8.10,
        "unit_cost_change_pct": 1.2
    },

    "q4_2025_financials": {
        "passengers_thousands": 24605,
        "passengers_growth_pct": 4.8,
        "capacity_million_sko": 83962,
        "capacity_growth_pct": 6.6,
        "traffic_million_pkt": 72228,
        "traffic_growth_pct": 4.9,
        "load_factor_pct": 86.0,
        "load_factor_change_pts": -1.3,
        "revenue_million_eur": 8186,
        "revenue_growth_pct": 3.9,
        "revenue_growth_constant_fx_pct": 6.7,
        "operating_result_million_eur": 393,
        "operating_result_change_million_eur": -3,
        "operating_margin_pct": 4.8,
        "operating_margin_change_pts": -0.2,
        "net_result_million_eur": 585,
        "net_result_change_million_eur": 606,
        "unit_revenue_per_sko_cents": 8.67,
        "unit_revenue_change_pct": -2.6,
        "unit_revenue_change_constant_fx_pct": -0.5,
        "unit_cost_per_sko_cents": 8.10,
        "unit_cost_change_pct": -1.1
    },

    "cashflow": {
        "2025": {
            "free_operating_cashflow_million_eur": 1997,
            "adjusted_recurring_free_operating_cashflow_million_eur": 1030
        },
        "2024": {
            "free_operating_cashflow_million_eur": 446,
            "adjusted_recurring_free_operating_cashflow_million_eur": 271
        }
    },

    "debt_metrics": {
        "2025_12_31": {
            "net_debt_million_eur": 8392,
            "current_ebitda_12m_million_eur": 5058,
            "net_debt_ebitda_ratio": 1.7
        },
        "2024_12_31": {
            "net_debt_million_eur": 7332,
            "current_ebitda_12m_million_eur": 4244,
            "net_debt_ebitda_ratio": 1.7
        }
    },

    "income_statement_annual": {
        "revenue_million_eur": 33007,
        "operating_charges_million_eur": -31003,
        "current_operating_result_million_eur": 2004,
        "operating_activities_result_million_eur": 2002,
        "net_financial_cost_million_eur": -431,
        "pre_tax_result_million_eur": 1863,
        "income_tax_million_eur": -123,
        "net_result_million_eur": 1754,
        "net_result_attributable_to_owners_million_eur": 1593,
        "minority_interests_million_eur": 161,
        "key_costs": {
            "aircraft_fuel_million_eur": -6406,
            "co2_quotas_million_eur": -346,
            "aeronautical_fees_million_eur": -2331,
            "staff_costs_million_eur": -9888,
            "depreciation_amortization_provisions_million_eur": -3054,
            "catering_million_eur": -975,
            "ground_handling_million_eur": -2178,
            "aeronautical_maintenance_million_eur": -3494
        }
    },

    "balance_sheet_2025_12_31": {
        "total_assets_million_eur": 39445,
        "non_current_assets_million_eur": 28883,
        "current_assets_million_eur": 10562,
        "total_equity_million_eur": 2364,
        "equity_attributable_to_owners_million_eur": 298,
        "minority_interests_equity_million_eur": 2066,
        "non_current_liabilities_million_eur": 19968,
        "current_liabilities_million_eur": 17113,
        "cash_and_equivalents_million_eur": 4714,
        "goodwill_million_eur": 223,
        "aeronautical_fixed_assets_million_eur": 13651,
        "right_of_use_assets_million_eur": 9452,
        "financial_debt_gross_million_eur": 15250,
        "net_debt_million_eur": 8392
    },

    "cashflow_statement_2025": {
        "operating_cashflow_million_eur": 5055,
        "investing_cashflow_million_eur": -2849,
        "financing_cashflow_million_eur": -2291,
        "net_change_in_cash_million_eur": -115,
        "capex_million_eur": -4449,
        "asset_disposal_proceeds_million_eur": 1391,
        "free_operating_cashflow_million_eur": 1997
    },

    "network_activity": {
        "full_year_2025": {
            "revenue_million_eur": 26114,
            "revenue_growth_pct": 3.8,
            "total_revenue_million_eur": 27243,
            "total_revenue_growth_pct": 3.6,
            "operating_result_million_eur": 1777,
            "operating_result_change_million_eur": 355,
            "operating_margin_pct": 6.5,
            "operating_margin_change_pts": 1.1,
            "passage_revenue_million_eur": 24114,
            "passage_revenue_growth_pct": 4.1,
            "cargo_revenue_million_eur": 2001,
            "cargo_revenue_growth_pct": 0.3
        },
        "q4_2025": {
            "revenue_million_eur": 6540,
            "revenue_growth_pct": 2.8,
            "total_revenue_million_eur": 6864,
            "total_revenue_growth_pct": 3.2,
            "operating_result_million_eur": 414,
            "operating_result_change_million_eur": -18,
            "operating_margin_pct": 6.0,
            "operating_margin_change_pts": -0.5
        }
    },

    "passage_network": {
        "full_year_2025": {
            "passengers_thousands": 76758,
            "passengers_growth_pct": 2.7,
            "capacity_million_sko": 283727,
            "capacity_growth_pct": 3.3,
            "traffic_million_pkt": 247354,
            "traffic_growth_pct": 2.8,
            "load_factor_pct": 87.2,
            "load_factor_change_pts": -0.4,
            "total_revenue_million_eur": 24828,
            "total_revenue_growth_pct": 4.0,
            "unit_revenue_per_sko_cents": 8.50,
            "unit_revenue_change_pct": 0.7,
            "unit_revenue_change_constant_fx_pct": 2.0
        },
        "q4_2025": {
            "passengers_thousands": 18856,
            "passengers_growth_pct": 2.0,
            "capacity_million_sko": 71344,
            "capacity_growth_pct": 4.3,
            "traffic_million_pkt": 61642,
            "traffic_growth_pct": 2.9,
            "load_factor_pct": 86.4,
            "load_factor_change_pts": -1.1,
            "total_revenue_million_eur": 6198,
            "total_revenue_growth_pct": 4.7,
            "unit_revenue_per_sko_cents": 8.39,
            "unit_revenue_change_pct": 0.0,
            "unit_revenue_change_constant_fx_pct": 2.2
        },
        "long_haul_annual": {
            "passengers_thousands": 27244,
            "passengers_growth_pct": 2.2,
            "capacity_million_sko": 231997,
            "capacity_growth_pct": 3.1,
            "traffic_million_pkt": 203938,
            "traffic_growth_pct": 2.6,
            "load_factor_pct": 87.9,
            "load_factor_change_pts": -0.5
        },
        "regional_breakdown_q4_2025": {
            "north_america": {
                "passengers_thousands": 2323,
                "passengers_growth_pct": 0.8,
                "traffic_million_pkt": 16625,
                "capacity_million_sko": 18880,
                "load_factor_pct": 88.1,
                "load_factor_change_pts": -0.5
            },
            "latin_america": {
                "passengers_thousands": 1000,
                "passengers_growth_pct": 11.0,
                "traffic_million_pkt": 9383,
                "capacity_million_sko": 10281,
                "load_factor_pct": 91.3,
                "load_factor_change_pts": 0.7
            },
            "asia_middle_east": {
                "passengers_thousands": 1659,
                "passengers_growth_pct": 9.5,
                "traffic_million_pkt": 12679,
                "capacity_million_sko": 14641,
                "load_factor_pct": 86.6,
                "load_factor_change_pts": -0.9
            },
            "africa": {
                "passengers_thousands": 986,
                "passengers_growth_pct": -3.5,
                "traffic_million_pkt": 6236,
                "capacity_million_sko": 7587,
                "load_factor_pct": 82.2,
                "load_factor_change_pts": -4.1
            },
            "caribbean_indian_ocean": {
                "passengers_thousands": 873,
                "passengers_growth_pct": 0.1,
                "traffic_million_pkt": 6434,
                "capacity_million_sko": 7493,
                "load_factor_pct": 85.9,
                "load_factor_change_pts": -2.1
            },
            "short_medium_haul": {
                "passengers_thousands": 12015,
                "passengers_growth_pct": 1.2,
                "traffic_million_pkt": 10284,
                "capacity_million_sko": 12462,
                "load_factor_pct": 82.5,
                "load_factor_change_pts": -1.5
            }
        }
    },

    "cargo": {
        "full_year_2025": {
            "tonnage_thousands_kg": 917,
            "tonnage_growth_pct": 0.8,
            "capacity_million_tko": 14693,
            "capacity_growth_pct": 2.5,
            "traffic_million_tkt": 6920,
            "traffic_growth_pct": 1.3,
            "load_factor_pct": 47.1,
            "load_factor_change_pts": -0.6,
            "total_revenue_million_eur": 2389,
            "total_revenue_change_pct": -0.1,
            "transport_revenue_million_eur": 2001,
            "transport_revenue_growth_pct": 0.3,
            "unit_revenue_per_tko_cents": 13.62,
            "unit_revenue_change_pct": -2.1,
            "unit_revenue_change_constant_fx_pct": -0.2
        },
        "q4_2025": {
            "tonnage_thousands_kg": 251,
            "tonnage_growth_pct": 0.5,
            "capacity_million_tko": 3758,
            "capacity_growth_pct": 3.8,
            "traffic_million_tkt": 1897,
            "traffic_growth_pct": 0.3,
            "load_factor_pct": 50.5,
            "load_factor_change_pts": -2.0,
            "total_revenue_million_eur": 661,
            "total_revenue_change_pct": -8.5,
            "transport_revenue_million_eur": 553,
            "transport_revenue_change_pct": -10.8,
            "unit_revenue_per_tko_cents": 14.72,
            "unit_revenue_change_pct": -14.1,
            "unit_revenue_change_constant_fx_pct": -10.7
        }
    },

    "transavia": {
        "full_year_2025": {
            "passengers_thousands": 26086,
            "passengers_growth_pct": 12.4,
            "capacity_million_sko": 52795,
            "capacity_growth_pct": 14.9,
            "traffic_million_pkt": 46131,
            "traffic_growth_pct": 13.2,
            "load_factor_pct": 87.4,
            "load_factor_change_pts": -1.3,
            "unit_revenue_per_sko_cents": 6.64,
            "unit_revenue_change_pct": -1.7,
            "unit_cost_per_sko_cents": 6.73,
            "unit_cost_change_pct": 1.2,
            "total_revenue_million_eur": 3451,
            "revenue_growth_pct": 12.3,
            "operating_result_million_eur": -52,
            "operating_margin_pct": -1.4,
            "operating_margin_change_pts": -1.5,
            "staff_costs_million_eur": -842,
            "fuel_costs_million_eur": -768,
            "other_operating_costs_million_eur": -1496,
            "depreciation_amortization_million_eur": -395
        },
        "q4_2025": {
            "passengers_thousands": 5749,
            "passengers_growth_pct": 15.1,
            "capacity_million_sko": 12618,
            "capacity_growth_pct": 21.8,
            "traffic_million_pkt": 10586,
            "traffic_growth_pct": 18.6,
            "load_factor_pct": 83.9,
            "load_factor_change_pts": -2.3,
            "unit_revenue_per_sko_cents": 5.87,
            "unit_revenue_change_pct": -6.3,
            "unit_cost_per_sko_cents": 6.45,
            "unit_cost_change_pct": -8.2,
            "total_revenue_million_eur": 737,
            "revenue_growth_pct": 13.7,
            "operating_result_million_eur": -73,
            "operating_result_change_million_eur": 11,
            "operating_margin_pct": -9.9,
            "operating_margin_change_pts": 3.0
        }
    },

    "maintenance_afiklm_em": {
        "full_year_2025": {
            "total_revenue_million_eur": 5570,
            "revenue_growth_pct": 9.5,
            "external_revenue_million_eur": 2307,
            "external_revenue_growth_pct": 10.6,
            "external_expenses_million_eur": -3590,
            "staff_costs_million_eur": -1261,
            "depreciation_amortization_million_eur": -452,
            "operating_result_million_eur": 267,
            "operating_result_change_million_eur": 97,
            "operating_margin_pct": 4.8,
            "operating_margin_change_pts": 1.5,
            "order_book_billion_usd_dec2025": 10.7,
            "order_book_billion_usd_dec2024": 8.7
        },
        "q4_2025": {
            "total_revenue_million_eur": 1423,
            "revenue_change_pct": -0.3,
            "external_revenue_million_eur": 582,
            "external_revenue_growth_pct": 0.7,
            "operating_result_million_eur": 46,
            "operating_result_change_million_eur": 0,
            "operating_margin_pct": 3.3,
            "operating_margin_change_pts": 0.0
        }
    },

    "air_france_group": {
        "full_year_2025": {
            "revenue_million_eur": 20242,
            "revenue_growth_pct": 5.3,
            "staff_costs_million_eur": -5759,
            "fuel_million_eur": -3860,
            "other_operating_costs_million_eur": -7342,
            "depreciation_amortization_million_eur": -1919,
            "operating_result_million_eur": 1362,
            "operating_result_change_million_eur": 382,
            "operating_margin_pct": 6.7,
            "operating_margin_change_pts": 1.6
        },
        "q4_2025": {
            "revenue_million_eur": 5026,
            "revenue_growth_pct": 3.8,
            "operating_result_million_eur": 256,
            "operating_result_change_million_eur": -46,
            "operating_margin_pct": 5.1,
            "operating_margin_change_pts": -1.1
        },
        "traffic_annual": {
            "passengers_thousands": 42294,
            "passengers_growth_pct": 1.2,
            "traffic_million_pkt": 148383,
            "capacity_million_sko": 171197,
            "load_factor_pct": 86.7,
            "load_factor_change_pts": -0.5
        }
    },

    "klm_group": {
        "full_year_2025": {
            "revenue_million_eur": 13205,
            "revenue_growth_pct": 3.9,
            "staff_costs_million_eur": -4108,
            "fuel_million_eur": -2547,
            "other_operating_costs_million_eur": -5002,
            "depreciation_amortization_million_eur": -1132,
            "operating_result_million_eur": 416,
            "operating_result_change_million_eur": 1,
            "operating_margin_pct": 3.2,
            "operating_margin_change_pts": -0.1,
            "back_on_track_program_contribution_min_million_eur": 450
        },
        "q4_2025": {
            "revenue_million_eur": 3269,
            "revenue_growth_pct": 3.5,
            "operating_result_million_eur": 78,
            "operating_result_change_million_eur": 27,
            "operating_margin_pct": 2.4,
            "operating_margin_change_pts": 0.8
        },
        "traffic_annual": {
            "passengers_thousands": 34464,
            "passengers_growth_pct": 4.4,
            "traffic_million_pkt": 98971,
            "capacity_million_sko": 112529,
            "load_factor_pct": 88.0,
            "load_factor_change_pts": -0.3
        }
    },

    "flying_blue_loyalty": {
        "full_year_2025": {
            "total_revenue_million_eur": 886,
            "revenue_change_million_eur": 75,
            "external_revenue_million_eur": 595,
            "external_revenue_change_million_eur": 59,
            "operating_result_million_eur": 218,
            "operating_result_change_million_eur": 18,
            "operating_margin_pct": 24.6,
            "members_million": 30,
            "airline_partners": 40,
            "commercial_partners": 100,
            "co_branded_credit_cards": 12
        },
        "q4_2025": {
            "total_revenue_million_eur": 241,
            "revenue_change_million_eur": 34,
            "external_revenue_million_eur": 162,
            "operating_result_million_eur": 58,
            "operating_result_change_million_eur": 14,
            "operating_margin_pct": 24.1,
            "operating_margin_change_pts": 2.8
        }
    },

    "roce": {
        "2025": {
            "average_capital_employed_million_eur": 12072,
            "adjusted_after_tax_result_million_eur": 1428,
            "roce_pct": 11.8
        },
        "2024": {
            "average_capital_employed_million_eur": 9694,
            "adjusted_after_tax_result_million_eur": 1173,
            "roce_pct": 12.1
        }
    },

    "sustainability": {
        "next_gen_fleet_pct_2025": 35,
        "next_gen_fleet_pct_2024": 27,
        "next_gen_fleet_target_2030_pct": 80,
        "saf_incorporation_rate_pct_2025": 2.9,
        "saf_incorporation_rate_pct_2024": 1.3,
        "saf_volume_thousand_tonnes_2025": 244,
        "legal_saf_obligation_pct": 1.2,
        "saf_target_2030_pct": 10,
        "saf_contracts_total_million_tonnes_to_2043": 3.5,
        "saf_suppliers": ["Neste", "DG Fuels", "SkyNRG", "TotalEnergies"],
        "ges_intensity_gco2eq_per_tkt_2025": 913,
        "ges_intensity_gco2eq_per_tkt_2024": 928,
        "ges_intensity_change_pct": -1.6,
        "ges_intensity_target_vs_2019_pct": -10,
        "ges_intensity_achieved_vs_2019_pct": -4.6,
        "chapter14_oaci_eligible_fleet_pct_2025": 42.7,
        "chapter14_oaci_eligible_fleet_pct_2024": 36.9,
        "women_top10pct_managers_2025": 36.6,
        "women_top10pct_managers_2024": 36.0,
        "women_top10pct_managers_target_2030": 40.0,
        "esg_ratings": {
            "cdp_climate": "A",
            "ecovadis": "Gold Medal (83/100)",
            "msci_esg": "BBB",
            "iss_esg": "Prime Status (C+)"
        },
        "sustainability_bond_penalty": {
            "reason": "GES intensity target not achieved by 2025",
            "may_2026_bond_premium_per_bond_eur": 750,
            "coupon_increase_pct_2027_2028": 0.375,
            "total_cost_impact_million_eur": 7.5
        }
    },

    "fleet": {
        "total_fleet_dec2025": 596,
        "operational_fleet_dec2025": 586,
        "change_vs_dec2024": 22,
        "long_haul_total": 189,
        "medium_haul_total": 298,
        "regional_total": 93,
        "cargo_total": 6,
        "aircraft_types": {
            "B777_300": {"air_france": 43, "klm": 16, "total": 59},
            "B777_200": {"air_france": 18, "klm": 15, "total": 33},
            "B787_9": {"air_france": 10, "klm": 13, "total": 23},
            "B787_10": {"air_france": 14, "klm": 1, "total": 14},
            "A350_900": {"air_france": 41, "klm": 3, "total": 41},
            "A330_200": {"air_france": 8, "klm": 6, "total": 14},
            "A330_300": {"air_france": 5, "klm": 0, "total": 5},
            "A321NEO": {"air_france": 12, "klm": 14, "transavia": 0, "total": 26},
            "A320NEO": {"transavia": 22, "total": 23},
            "A220_300": {"air_france": 52, "klm": 0, "total": 52},
            "B737_800": {"klm": 103, "transavia": 30, "total": 131},
            "Embraer_195_E2": {"air_france_hop": 25, "total": 25},
            "Embraer_190": {"air_france_hop": 27, "klm_cityhopper": 20, "total": 45}
        }
    },

    "ma_transactions": {
        "sas": {
            "current_stake_pct": 19.9,
            "target_stake_pct": 60.5,
            "announcement_date": "2025-07-04",
            "expected_completion": "H2 2026",
            "danish_state_retains_pct": 26.4,
            "sellers": ["Castlelake", "Lind Invest"],
            "sky_team_member": True,
            "commercial_cooperation_since": "Summer 2024"
        },
        "westjet": {
            "af_klm_stake_pct": 2.3,
            "delta_stake_pct": 12.7,
            "korean_air_stake_pct": 10.0,
            "combined_stake_pct": 25.0,
            "announcement_date": "2025-10-23",
            "seller": "Onex Partners",
            "westjet_rank_among_afklm_partners_by_revenue": 6,
            "partnership_since": 2009
        }
    },

    "debt_operations_2025": [
        {
            "month": "January 2025",
            "type": "Bond repayment",
            "amount_million_eur": 515.2,
            "isin": "FR0014477254",
            "coupon_pct": 1.875
        },
        {
            "month": "May 2025",
            "type": "Hybrid bond issuance",
            "amount_million_eur": 500,
            "oversubscription_times": 3.5,
            "coupon_pct": 5.75,
            "yield_pct": 5.875,
            "fitch_rating": "BB",
            "sp_rating": "B+"
        },
        {
            "month": "July 2025",
            "type": "Hybrid perpetual bond repayment",
            "amount_million_eur": 500,
            "notes": "Issued July 2022, subscribed by Apollo affiliates"
        },
        {
            "month": "August 2025",
            "type": "Senior unsecured bond issuance (EMTN)",
            "amount_million_eur": 500,
            "maturity_years": 5,
            "coupon_pct": 3.75,
            "yield_pct": 3.866
        },
        {
            "month": "November 2025",
            "type": "Convertible hybrid bond early redemption",
            "amount_million_eur": 305,
            "price_per_bond_eur": 100000
        }
    ],

    "post_period_events": {
        "jan_2026_weather_disruptions": {
            "locations": ["Amsterdam", "Paris"],
            "estimated_q1_2026_operating_impact_million_eur": -90
        },
        "jan_2026_bond_issuance": {
            "type": "Senior unsecured EMTN",
            "amount_million_eur": 650,
            "maturity_years": 5,
            "coupon_pct": 3.875,
            "yield_pct": 4.033,
            "original_size_million_eur": 500,
            "proceeds_use": "General corporate purposes + May 2026 bond repayment (500M EUR, 7.25% coupon)"
        }
    },

    "fuel_hedging_policy": {
        "effective_date": "2026-01-01",
        "hedging_horizon_quarters_old": 6,
        "hedging_horizon_quarters_new": 8,
        "annual_exposure_old_pct": 68,
        "annual_exposure_new_pct": 87,
        "hedging_schedule_new": {
            "current_quarter": 70,
            "T_plus_1": 70,
            "T_plus_2": 60,
            "T_plus_3": 50,
            "T_plus_4": 40,
            "T_plus_5": 30,
            "T_plus_6": 20,
            "T_plus_7": 10
        }
    },

    "outlook_2026": {
        "capacity_growth_pct": "3% to 5%",
        "unit_cost_change_pct": "0% to +2%",
        "unit_cost_premiumisation_contribution_pct": 0.5,
        "net_capex_billion_eur": 3.0,
        "net_debt_ebitda_target": "1.5x to 2.0x",
        "capacity_breakdown": {
            "long_haul_network": "+4%",
            "short_medium_haul_network": "stable",
            "transavia": "+10%"
        }
    },

    "outlook_2028": {
        "operating_margin_target_pct": ">8%",
        "free_cashflow": "significantly positive",
        "unit_cost_direction": "reduction",
        "leverage_target": "investment grade",
        "drivers": [
            "Premiumisation",
            "Cost discipline",
            "Fleet renewal",
            "Ongoing transformation"
        ]
    }
}

output_path = "/mnt/user-data/outputs/airfranceklm_annual_results_2025.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"JSON file saved to: {output_path}")
print(f"Total top-level keys: {len(data)}")
print("Keys:", list(data.keys()))
