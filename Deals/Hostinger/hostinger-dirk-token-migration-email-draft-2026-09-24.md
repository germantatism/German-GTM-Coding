# Dirk's draft: token migration follow-up to Paulius (Sep 24, 2026)

**Status:** draft shared by Dirk with German on Sep 24, 2026. Sequence agreed: German's recap goes first, Dirk's note follows in the same thread.

**Issues flagged before sending (German, Sep 24):**
1. Network tokens: the draft says NTs are not portable between token requestors and that Yuno provisions fresh tokens under a merchant-scoped requestor ID operated for Hostinger. Antoine in the Slack group the same morning: Hostinger has its own TRID, "they need to do some paperwork to make us the TR-TSP, nothing ground breaking, we can import their tokens." Paulius asked this directly on the call. Align Dirk and Antoine before sending.
2. Stray text in the Monitors bullet ("SpaceX/Starlink India compliance answer.") and broken phrases ("market andemail or Opsgenie", "if aprovider").
3. Retry timing for charges initiated by Hostinger's billing engine is not covered; it was Paulius's concrete ask.

---

Paulius,

Thanks for the time today. Here's how a migration of your token base actually runs, and what we do so your approval rate doesn't dip on the way through.

We run the migration directly with your current token provider. Your team's only real task is swapping one set of identifiers for another once we hand you the mapping file. No shopper re-enters a card, no renewal is interrupted, and every stage is reversible.

What we take from your current provider, for each stored card:

- Their token or card reference ID, so we can give you a row-by-row mapping back
- The card number and expiry
- Cardholder name
- The network transaction ID, which is the scheme reference from the original transaction in each recurring series
- The PAR where they hold them

The network transaction ID is the field most often left out of a migration, and it's the most common reason approval rates fall afterwards. It tells the issuer that a renewal continues a series the cardholder already agreed to. Without it, every one of your subscriptions looks like a brand new first payment. At Yuno, we always include this element in the token migration, to ensure your performance doesn't dip during or shortly after the migration.

The transfer itself is a PGP-encrypted file over SFTP against your provider's allowlisted IPs. We've done this with Adyen, Stripe, Primer and Unlimit among others, so in most cases we're asking their migrations team for something they've run before.

What happens on our side
We validate every record, deduplicate by card fingerprint and PAR, and return two files:

- Mapping report of old reference to Yuno token
- Rejects report with a reason per row, so you can see exactly what didn't come across and why (most often caused by expired cards)

On network tokens, these aren't portable between token requestors, which is a scheme constraint rather than a Yuno one. This means that we cannot authenticate against the tokens that your current provider holds. The path we'd stand behind either way: your provider releases PANs, expiry and network transaction IDs, we vault them and provision fresh network tokens under a merchant-scoped requestor ID we operate for Hostinger. No cardholder re-entry, and the stored-credential chain is preserved through the network transaction IDs, which is the part that protects your renewal auth rate.

How we protect the auth rate
As mentioned, we make sure to retain the NTID during the migration process. Additionally, we don't move all your tokens in one night. The migration runs in waves, each gated on live performance:

- Pilot, 1–2%. A matched sample across your main markets and card mixes, run for a full billing cycle.
- 10%, once the pilot clears.
- 50%.
- The remainder.

Each wave has an agreed approval-rate threshold before the next one opens. Your old tokens stay live until the final wave clears, meaning that a rollback is possible at any point in time.

Running underneath all of it, to optimise your performance as much as possible:

- Account Updater from day one, so cards reissued mid-migration refresh themselves instead of failing
- Stored-credential flags set correctly per scheme for each charge type, which issuers increasingly enforce
- Monitors on approval rate by provider, market andemail or Opsgenie, with automatic rerouting if aprovider starts underperforming    SpaceX/Starlink India compliance answer.

India:
India is a different topic, and we have set out the question with our Token and Vault team. First messages are promising, and we'll get back to you as soon as we have a clear picture on that.

Happy to put in some time to go over this process in detail if you wish. Please let us know.

Best,
