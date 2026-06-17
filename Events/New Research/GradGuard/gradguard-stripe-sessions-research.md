# GRADGUARD | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: GradGuard
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/idxE8BC0cM/idZ3nM5jYO.svg
Nombre merchant: GradGuard

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single Acquirer Risk
Tittle_Pain Point_2: No Recurring Retry Logic
Tittle_Pain Point_3: Limited Payment Options
Tittle_Pain Point_4: Enrollment Season Spikes
Tittle_Pain Point_5: No Cross-Border Coverage

Desc_Pain Point_1: GradGuard processes all insurance premium payments through a single card acquirer. Any outage during enrollment deadlines blocks policy purchases for 650,000+ students across 600+ partner universities with zero fallback processor.
Desc_Pain Point_2: Monthly payment plan subscribers are billed 18 days before each coverage period. If the card on file declines, there is no automated cascade or retry through an alternate acquirer, risking policy lapse and coverage gaps for students mid-semester.
Desc_Pain Point_3: GradGuard accepts only credit/debit cards and eCheck (QuikPay). No ACH Direct Debit, no PayPal, no digital wallets, no BNPL options. Parents paying $120 to $220 per semester per $10K in coverage have limited ways to complete the purchase.
Desc_Pain Point_4: Insurance purchases concentrate in two annual enrollment windows before fall and spring semesters. Processing 600+ universities' students through a single acquirer during these peaks creates transaction volume spikes that increase decline rates.
Desc_Pain Point_5: GradGuard serves international students studying in the US but offers no payment methods for families paying from abroad. No local bank transfers, no international wallets, no FX-optimized checkout for parents in Asia, Europe, or Latin America.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (card processing)
PSP_2: QuikPay (eCheck)
PSP_3: Jefferson Insurance (underwriter)
PSP_4: Allianz Partners (admin)
PSP_5: N/A

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: ACH Direct Debit
Local_M_2: PayPal
Local_M_3: Apple Pay
Local_M_4: Google Pay
Local_M_5: Venmo
Local_M_6: Alipay
Local_M_7: WeChat Pay
Local_M_8: UPI
Local_M_9: SEPA Direct Debit
Local_M_10: Pix

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every insurance premium payment to the best performing acquirer by card BIN, issuing bank, and parent location. With 1.7M+ students served across 600+ universities, a 3% auth uplift during enrollment windows recovers thousands of otherwise lost policy sales per semester.
Desc_Yuno_Cap2: When a monthly installment payment declines, Yuno cascades to an alternate acquirer in milliseconds. Recovers up to 50% of failed recurring charges, directly preventing policy lapses that leave students without tuition protection mid-semester.
Desc_Yuno_Cap3: Unlocks the payment methods GradGuard's diverse student base needs: ACH and PayPal for US parents, Alipay and WeChat Pay for Chinese families (1M+ Chinese students in the US), UPI for Indian families, SEPA DD for European parents. One API, 1,000+ payment methods, zero engineering sprints per market.
Desc_Yuno_Cap4: Single dashboard consolidating card processing, eCheck (QuikPay), and new payment rails into one view. Real-time auth rate monitoring across enrollment peaks at 600+ universities, centralized reconciliation with Allianz/Jefferson Insurance, and millisecond anomaly detection via NOVA.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**GradGuard at a glance:**
- Founded: 2009 (venture of Next Generation Insurance Group, LLC)
- CEO/Co-Founder: John Fees (Arizona State, Harvard Business School)
- Co-Founder: Bill Suneson
- COO: Jeff Hitchens (joined December 2020)
- CFO: Colin Brennan (joined October 2022)
- Headquarters: 5333 N 7th St, Phoenix, AZ
- Employees: 11 to 50
- Products: Tuition Insurance, Renters Insurance (dorm/off-campus)
- Insurance underwriter: Jefferson Insurance Company (A.M. Best "A+" rated)
- Administrator: AGA Service Company (dba Allianz Partners/Allianz Global Assistance)
- University partners: 600+ colleges and universities with embedded enrollment
- Students served: 1.7M+ at 1,900+ unique institutions
- Students with access via school-sponsored programs: 650,000+ across 300+ programs
- Market served: 18M+ college students investing $500B+/year in US higher education
- Pricing: Tuition insurance $120 to $220 per $10,000 covered per semester (max $50K/term); Renters insurance $9 to $17/month for $7,500 coverage
- Recognition: Top 100 Financial Technology Companies of 2024 (Financial Technology Report)
- Funding: Private/bootstrapped; no publicly disclosed venture rounds found
- Operations: US only (but serves international students studying in the US)

**Confirmed PSPs / payment methods:**
- Card processing via single acquirer (Stripe confirmed by attending Stripe Sessions; job listings reference Stripe integration)
- eCheck via QuikPay for direct bank payment
- Credit/debit cards accepted
- No digital wallets detected (no Apple Pay, Google Pay, PayPal)
- No ACH Direct Debit option
- No payment orchestrator detected
- No international payment methods detected

**Payment issues documented:**
- Billing cycle: annual plan charged at purchase date; monthly plan charged 18 days before each new period
- Policy structure complaints: policyholder must be the student (not the paying parent)
- Policy state must match the educational institution's state, not student's residence state
- Preexisting conditions exclusion: students who may most need coverage are excluded
- Limited coverage scenarios: school closure, family issues, parental job loss, caretaker situations not covered
- No transparent way to review specific policy terms on the website before purchase
- Cancellation: must call 877-794-6603; refund of unearned premium only if no claim initiated
- Policy Administration Fee added to all policies (specific amount not disclosed publicly)

**Key meeting angles:**
1. **Enrollment deadline pressure**: 600+ universities with concentrated purchase windows create peak processing demands; multi-acquirer routing prevents decline spikes
2. **International student families**: Over 1M Chinese students, 200K+ Indian students in the US; their families need Alipay, WeChat Pay, UPI to pay insurance premiums from abroad
3. **Monthly payment recovery**: Recurring billing with no retry/failover means every declined card = policy lapse = unprotected student
4. **$500B market opportunity**: GradGuard protects a fraction of the $500B annual higher education investment; better checkout conversion = more insured students
5. **Parent as payer**: Parents typically pay but cannot be the policyholder; offering PayPal, ACH, and wallets gives parents more flexibility
6. **Embedded enrollment advantage**: 600+ universities embed GradGuard in their enrollment process; seamless checkout with more payment options increases conversion at the point of enrollment

**Sources:**
- [GradGuard Official Website](https://gradguard.com/)
- [GradGuard About Us](https://gradguard.com/about-us)
- [GradGuard Tuition Insurance](https://gradguard.com/tuition)
- [GradGuard International Students](https://gradguard.com/international-students)
- [GradGuard Billing FAQ](https://gradguard.com/support/faq/360033655931)
- [GradGuard Update Billing Info](https://gradguard.com/support/faq/360058633991)
- [GradGuard Insurance FAQs](https://gradguard.com/insurance-faqs)
- [GradGuard Policy Administration Fee](https://gradguard.com/support/faq/22927384274196)
- [GradGuard Network Surpasses 600 Schools (PRNewswire)](https://www.prnewswire.com/news-releases/gradguard-network-of-colleges-and-universities-surpasses-600-school-partners-302201060.html)
- [GradGuard Top 100 FinTech 2024](https://hub.gradguard.com/knowledge-center/gradguard-named-top-fintech-company-2024)
- [GradGuard Insurance Review (The College Investor)](https://thecollegeinvestor.com/42409/gradguard-review/)
- [GradGuard Review (BlogMelon)](https://www.blogmelon.com/gradguard-insurance-review-pros-cons/)
- [GradGuard Bogleheads Discussion](https://www.bogleheads.org/forum/viewtopic.php?t=353150)
- [GradGuard Crunchbase](https://www.crunchbase.com/organization/gradguard)
- [GradGuard The Org](https://theorg.com/org/gradguard)
- [Allianz Tuition Protection Expansion (PRNewswire)](https://www.prnewswire.com/news-releases/allianz-expands-tuition-protection-offerings-to-colleges-and-universities-300450462.html)
