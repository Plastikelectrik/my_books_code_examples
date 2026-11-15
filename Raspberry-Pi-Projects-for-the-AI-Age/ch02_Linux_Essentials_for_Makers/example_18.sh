ssh-keygen -t ed25519 -C "my laptop"
ssh-copy-id oscar@pi5.local
ssh oscar@pi5.local     # now works without a password
