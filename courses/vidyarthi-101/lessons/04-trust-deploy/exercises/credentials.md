# Exercise — issue and verify a credential

Using `src/vidyarthi/credentials.py`:

1. Generate an issuer keypair and build a `community` credential for
   `vidyarthi:platform:101` bound to your learner identifier and the current
   course revision.
2. Sign it, verify it, then tamper with one outcome and verify again.
3. Append the issuance to an `AppendOnlyCredentialLog`, revoke it with a reason,
   and run `verify_chain`. Explain why revocation is a new record (§8.2).
