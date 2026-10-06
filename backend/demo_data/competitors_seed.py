"""
Curated competitive intelligence historical events for demonstration.
Clearly labeled as DEMO DATA.
"""
from typing import List, Dict

COMPETITORS_METADATA = [
    {
        "id": "stripe",
        "name": "Stripe",
        "industry": "Fintech & Payments",
        "description": "Global financial infrastructure platform, strategically pivoting from developer-first SMB self-serve to high-margin Global 2000 enterprise accounts.",
        "tags": ["Payments", "API", "Enterprise", "AI Agent Billing", "Global Treasury"],
        "key_themes": ["Enterprise Up-market Migration", "Autonomous AI Billing Primitives", "Bifurcated Monetization"]
    },
    {
        "id": "razorpay",
        "name": "Razorpay",
        "industry": "Fintech & Payments",
        "description": "Full-stack financial services and payments leader in India and Southeast Asia, integrating omnichannel POS, payroll SaaS, and cross-border corridors.",
        "tags": ["UPI", "Southeast Asia", "Full-Stack B2B", "Payroll SaaS", "IPO Preparation"],
        "key_themes": ["Cross-Border Corridor Expansion", "Omnichannel Biometric POS", "Margin Consolidation Ahead of IPO"]
    },
    {
        "id": "paypal",
        "name": "PayPal",
        "industry": "Digital Payments",
        "description": "Digital payments and consumer wallet incumbent focused on Fastlane guest checkout defense, unbranded Braintree processing, and PYUSD stablecoin settlement.",
        "tags": ["Fastlane", "Venmo", "PYUSD Stablecoin", "Consumer Checkout", "Amazon Partnership"],
        "key_themes": ["Guest Checkout Defense vs Shopify", "B2B Stablecoin Settlement", "Consumer Cross-Subsidization"]
    }
]

SEED_EVENTS: List[Dict] = [
    # -------------------------------------------------------------------------
    # STRIPE (11 Historical Events)
    # -------------------------------------------------------------------------
    {
        "id": "stripe-01",
        "competitor": "Stripe",
        "category": "Pricing",
        "date": "JAN 2026",
        "title": "Lower-Cost Base Plan for Startups",
        "description": "Stripe unbundled its core processing fees, introducing a lower-cost base plan for early-stage startups that waives fees on first $25k in annual processing volume.",
        "source": "Stripe Pricing Bulletin [DEMO DATA]",
        "tags": ["pricing", "startups", "unbundling"]
    },
    {
        "id": "stripe-02",
        "competitor": "Stripe",
        "category": "Product",
        "date": "FEB 2026",
        "title": "AI-Powered Fraud Detection Launched",
        "description": "Stripe launched an advanced AI-powered Radar upgrade featuring autonomous agentic dispute reasoning to detect synthetic identity fraud and automate merchant chargeback filings.",
        "source": "Stripe Newsroom [DEMO DATA]",
        "tags": ["product", "ai", "fraud", "radar"]
    },
    {
        "id": "stripe-03",
        "competitor": "Stripe",
        "category": "Marketing",
        "date": "MAR 2026",
        "title": "Enterprise-Focused Messaging Overhaul",
        "description": "Stripe completely overhauled its marketing messaging and homepage copy, shifting prominence away from developer code snippets to Fortune 500 multi-processor orchestration and guaranteed uptime SLAs.",
        "source": "Wall Street Journal FinTech Analysis [DEMO DATA]",
        "tags": ["marketing", "enterprise", "positioning"]
    },
    {
        "id": "stripe-04",
        "competitor": "Stripe",
        "category": "Partnership",
        "date": "APR 2026",
        "title": "Strategic Enterprise Co-Selling Partnership",
        "description": "Stripe announced a global strategic enterprise partnership with Salesforce, embedding Stripe billing and invoicing directly into Salesforce Financial Services Cloud with joint enterprise sales incentives.",
        "source": "Salesforce & Stripe Press Release [DEMO DATA]",
        "tags": ["partnership", "salesforce", "enterprise"]
    },
    {
        "id": "stripe-05",
        "competitor": "Stripe",
        "category": "Product",
        "date": "MAY 2026",
        "title": "Developer Platform AI Agent Billing Primitives",
        "description": "Stripe unveiled programmable billing primitives designed specifically for autonomous AI agents, enabling software agents to negotiate micro-quotas and settle dynamic API compute tokens.",
        "source": "Stripe Developer Changelog [DEMO DATA]",
        "tags": ["product", "ai-agents", "developer-platform"]
    },
    {
        "id": "stripe-06",
        "competitor": "Stripe",
        "category": "Pricing",
        "date": "JUN 2026",
        "title": "Enterprise Pricing Restructuring",
        "description": "Stripe rolled out updated enterprise pricing schedules that raised minimum annual commitment thresholds while bundling dedicated technical account managers and custom fraud rules.",
        "source": "Enterprise Client Circular [DEMO DATA]",
        "tags": ["pricing", "enterprise", "volume-tiers"]
    },
    {
        "id": "stripe-07",
        "competitor": "Stripe",
        "category": "Hiring",
        "date": "JUL 2026",
        "title": "Enterprise Sales VP Recruited from Oracle",
        "description": "Stripe hired Oracle's Global VP of Financial Applications to head their North American enterprise sales team, accompanied by 40 senior corporate account executives.",
        "source": "LinkedIn Executive Hiring Telemetry [DEMO DATA]",
        "tags": ["hiring", "enterprise", "sales-leadership"]
    },
    {
        "id": "stripe-08",
        "competitor": "Stripe",
        "category": "Product",
        "date": "AUG 2026",
        "title": "Global Enterprise Treasury Suite Launch",
        "description": "Stripe launched Enterprise Treasury Suite, providing automated multi-currency yield management, cross-border FX routing, and real-time liquidity sweeping for multinational corporations.",
        "source": "Fintech Today [DEMO DATA]",
        "tags": ["product", "treasury", "enterprise", "fx"]
    },
    {
        "id": "stripe-09",
        "competitor": "Stripe",
        "category": "Product",
        "date": "SEP 2026",
        "title": "Corporate Virtual Card Kit for Agent Spending",
        "description": "Introduced corporate issuing controls enabling enterprise finance departments to assign real-time cryptographic spend limits to generative AI agents and autonomous workflows.",
        "source": "TechCrunch Enterprise [DEMO DATA]",
        "tags": ["product", "issuing", "ai", "enterprise"]
    },
    {
        "id": "stripe-10",
        "competitor": "Stripe",
        "category": "Strategy",
        "date": "OCT 2026",
        "title": "Enterprise Orchestration & Multi-Processor Routing",
        "description": "Formally released Stripe Orchestration, allowing enterprise merchants to route overflow volume across multiple legacy merchant acquirers while maintaining single-dashboard reporting.",
        "source": "Stripe Keynote Telemetry [DEMO DATA]",
        "tags": ["strategy", "enterprise", "orchestration"]
    },
    {
        "id": "stripe-11",
        "competitor": "Stripe",
        "category": "Customer Reaction",
        "date": "NOV 2026",
        "title": "Enterprise Migration Case Studies Released",
        "description": "Published verified enterprise adoption metrics revealing 42% reduction in payment routing failures across 15 newly migrated Fortune 500 retail chains.",
        "source": "Stripe Enterprise Case Studies [DEMO DATA]",
        "tags": ["customer-reaction", "enterprise", "case-studies"]
    },

    # -------------------------------------------------------------------------
    # RAZORPAY (11 Historical Events)
    # -------------------------------------------------------------------------
    {
        "id": "razorpay-01",
        "competitor": "Razorpay",
        "category": "Market",
        "date": "OCT 2025",
        "title": "Southeast Asia Payment Licensing Expansion",
        "description": "Razorpay secured major payment institution licenses in Singapore and Malaysia, establishing direct connectivity with regional PayNow and DuitNow rails.",
        "source": "DealStreetAsia [DEMO DATA]",
        "tags": ["market", "sea", "cross-border", "licensing"]
    },
    {
        "id": "razorpay-02",
        "competitor": "Razorpay",
        "category": "Product",
        "date": "NOV 2025",
        "title": "Turbo UPI 2.0 Sub-Second Checkout Launch",
        "description": "Debuted Turbo UPI 2.0, providing an in-app 1-click checkout that achieves 99.8% success rates without browser redirect drop-offs for top Indian merchants.",
        "source": "Razorpay Product Blog [DEMO DATA]",
        "tags": ["product", "upi", "checkout", "mobile"]
    },
    {
        "id": "razorpay-03",
        "competitor": "Razorpay",
        "category": "Pricing",
        "date": "DEC 2025",
        "title": "0% MDR Subsidies for Incubator Startups",
        "description": "Instituted a 0% merchant discount rate (MDR) policy for incubator-backed tech startups on UPI and domestic debit card transactions up to 50 Lakhs.",
        "source": "Economic Times [DEMO DATA]",
        "tags": ["pricing", "startups", "mdr", "subsidies"]
    },
    {
        "id": "razorpay-04",
        "competitor": "Razorpay",
        "category": "Product",
        "date": "JAN 2026",
        "title": "Ray Conversational AI Financial Co-Pilot",
        "description": "Launched 'Ray', an AI co-pilot inside Razorpay Dashboard capable of answering natural language queries on GST filing, invoice discrepancies, and cash runway forecasts.",
        "source": "Razorpay FTX Showcase [DEMO DATA]",
        "tags": ["product", "ai", "cfo", "co-pilot"]
    },
    {
        "id": "razorpay-05",
        "competitor": "Razorpay",
        "category": "Partnership",
        "date": "FEB 2026",
        "title": "NPCI European Cross-Border Payment Alliance",
        "description": "Forged a partnership with NPCI International to facilitate inbound e-commerce and tourism transactions between European financial institutions and Indian UPI merchants.",
        "source": "Business Standard [DEMO DATA]",
        "tags": ["partnership", "npci", "cross-border", "europe"]
    },
    {
        "id": "razorpay-06",
        "competitor": "Razorpay",
        "category": "Strategy",
        "date": "MAR 2026",
        "title": "Acquisition of Automated B2B Payroll SaaS",
        "description": "Acquired a leading enterprise payroll and tax software provider, integrating payroll disbursement directly into merchant working-capital lending facilities.",
        "source": "LiveMint [DEMO DATA]",
        "tags": ["strategy", "m&a", "payroll", "b2b"]
    },
    {
        "id": "razorpay-07",
        "competitor": "Razorpay",
        "category": "Pricing",
        "date": "APR 2026",
        "title": "Dynamic Risk-Adjusted Processing Rates",
        "description": "Rolled out risk-adjusted fee schedules that dynamically discount processing costs by up to 15 bps for merchants maintaining chargeback ratios below 0.05%.",
        "source": "Merchant Advisory Bulletin [DEMO DATA]",
        "tags": ["pricing", "risk", "margins"]
    },
    {
        "id": "razorpay-08",
        "competitor": "Razorpay",
        "category": "Hiring",
        "date": "MAY 2026",
        "title": "AWS FinTech Architecture Head Hired as CTO",
        "description": "Appointed former AWS Head of Cloud FinTech Architecture as Chief Technology Officer to lead multi-region high-availability infrastructure modernization.",
        "source": "YourStory FinTech [DEMO DATA]",
        "tags": ["hiring", "cto", "cloud", "resilience"]
    },
    {
        "id": "razorpay-09",
        "competitor": "Razorpay",
        "category": "Product",
        "date": "JUN 2026",
        "title": "Acoustic Biometric Smart Soundbox POS",
        "description": "Debuted next-generation retail hardware combining acoustic audio tone confirmation with biometric fingerprint authorization for high-volume retail chains.",
        "source": "Retail Technology Times [DEMO DATA]",
        "tags": ["product", "hardware", "pos", "retail"]
    },
    {
        "id": "razorpay-10",
        "competitor": "Razorpay",
        "category": "Marketing",
        "date": "JUL 2026",
        "title": "D2C Direct-to-Consumer Growth Campaign",
        "description": "Launched a nationwide promotional campaign bundling Magic Checkout with predictive RTO (Return-to-Origin) logistics protection for 10,000 emerging retail brands.",
        "source": "Inc42 [DEMO DATA]",
        "tags": ["marketing", "d2c", "logistics", "checkout"]
    },
    {
        "id": "razorpay-11",
        "competitor": "Razorpay",
        "category": "Strategy",
        "date": "SEP 2026",
        "title": "Pre-IPO Domestic Corporate Restructuring",
        "description": "Completed full corporate redomiciliation back to India and filed draft IPO prospectus showcasing 38% year-over-year gross profit margin expansion.",
        "source": "Bloomberg India [DEMO DATA]",
        "tags": ["strategy", "ipo", "governance", "margins"]
    },

    # -------------------------------------------------------------------------
    # PAYPAL (11 Historical Events)
    # -------------------------------------------------------------------------
    {
        "id": "paypal-01",
        "competitor": "PayPal",
        "category": "Product",
        "date": "OCT 2025",
        "title": "PayPal Complete Payments SMB Platform Refresh",
        "description": "Overhauled PayPal Complete Payments (PPCP) for small merchants with turnkey support for Apple Pay, Google Pay, and localized European debit wallets.",
        "source": "PayPal Investor Relations [DEMO DATA]",
        "tags": ["product", "smb", "wallets", "checkout"]
    },
    {
        "id": "paypal-02",
        "competitor": "PayPal",
        "category": "Pricing",
        "date": "NOV 2025",
        "title": "Consumer Cross-Border FX Spread Hike",
        "description": "Increased consumer peer-to-peer foreign currency conversion spreads from 3.0% to 3.4% to safeguard consumer division contribution margins.",
        "source": "User Agreement Policy Update [DEMO DATA]",
        "tags": ["pricing", "fx", "consumer", "margins"]
    },
    {
        "id": "paypal-03",
        "competitor": "PayPal",
        "category": "Marketing",
        "date": "DEC 2025",
        "title": "Fastlane Guest Checkout Go-To-Market Blitz",
        "description": "Launched an aggressive marketing blitz for Fastlane guest checkout across BigCommerce and WooCommerce retailers with claims of 80% recognition and 40% faster checkout.",
        "source": "Retail Dive [DEMO DATA]",
        "tags": ["marketing", "fastlane", "guest-checkout"]
    },
    {
        "id": "paypal-04",
        "competitor": "PayPal",
        "category": "Product",
        "date": "JAN 2026",
        "title": "AI Personalized Merchant Offers Engine",
        "description": "Integrated an AI-driven merchant recommendation engine directly inside the consumer PayPal mobile app to drive repeat purchases at partner stores.",
        "source": "PayPal Product Showcase [DEMO DATA]",
        "tags": ["product", "ai", "rewards", "consumer"]
    },
    {
        "id": "paypal-05",
        "competitor": "PayPal",
        "category": "Strategy",
        "date": "FEB 2026",
        "title": "Operational Streamlining & Braintree Focus",
        "description": "Reduced non-engineering administrative headcount by 9% globally to reallocate capital toward unbranded Braintree enterprise infrastructure deployment.",
        "source": "SEC Form 8-K [DEMO DATA]",
        "tags": ["strategy", "efficiency", "braintree", "margins"]
    },
    {
        "id": "paypal-06",
        "competitor": "PayPal",
        "category": "Partnership",
        "date": "MAR 2026",
        "title": "Multi-Year Amazon Buy with Prime Extension",
        "description": "Expanded strategic alliance with Amazon enabling PayPal wallet and Fastlane integration across off-Amazon merchants utilizing the Buy with Prime program.",
        "source": "Amazon Press Center [DEMO DATA]",
        "tags": ["partnership", "amazon", "prime", "fastlane"]
    },
    {
        "id": "paypal-07",
        "competitor": "PayPal",
        "category": "Pricing",
        "date": "APR 2026",
        "title": "Fastlane Merchant Incentive Fee Rebates",
        "description": "Introduced a 10 bps transaction fee rebate for e-commerce merchants who route at least 60% of guest checkout volume through Fastlane.",
        "source": "Merchant Partner Circular [DEMO DATA]",
        "tags": ["pricing", "incentives", "fastlane", "volume"]
    },
    {
        "id": "paypal-08",
        "competitor": "PayPal",
        "category": "Product",
        "date": "MAY 2026",
        "title": "Venmo Teen Debit & Smart Parental Guardrails",
        "description": "Launched Venmo Teen accounts featuring customizable AI spending boundaries, real-time parental notifications, and zero-balance overdraft blocks.",
        "source": "Venmo Newsroom [DEMO DATA]",
        "tags": ["product", "venmo", "teens", "consumer"]
    },
    {
        "id": "paypal-09",
        "competitor": "PayPal",
        "category": "Hiring",
        "date": "JUN 2026",
        "title": "Chief Risk Officer Recruited from Capital One",
        "description": "Hired veteran consumer analytics executive as Chief Risk Officer to oversee automated merchant credit underwriting and real-time transaction scoring.",
        "source": "American Banker [DEMO DATA]",
        "tags": ["hiring", "risk", "credit", "leadership"]
    },
    {
        "id": "paypal-10",
        "competitor": "PayPal",
        "category": "Strategy",
        "date": "JUL 2026",
        "title": "Zero-Gas Fee PYUSD Settlement on Braintree",
        "description": "Enabled international B2B merchants on Braintree to settle cross-border supplier balances directly in PayPal USD (PYUSD) stablecoin with zero gas fees.",
        "source": "CoinDesk / Reuters [DEMO DATA]",
        "tags": ["strategy", "crypto", "pyusd", "braintree", "settlement"]
    },
    {
        "id": "paypal-11",
        "competitor": "PayPal",
        "category": "Product",
        "date": "SEP 2026",
        "title": "100% Merchant Passkey Biometric Rollout",
        "description": "Completed deployment of FIDO2-certified biometric passkey authentication across all North American merchant checkouts, eliminating password friction.",
        "source": "Wired Security [DEMO DATA]",
        "tags": ["product", "security", "passkeys", "biometrics"]
    }
]
