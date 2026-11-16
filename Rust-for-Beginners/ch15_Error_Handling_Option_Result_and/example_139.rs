// Book: Rust for Beginners — Example 139
use std::fmt;

#[derive(Debug)]
enum WithdrawError {
    InsufficientFunds { needed: u32, available: u32 },
    AccountFrozen,
    InvalidAmount,
}

impl fmt::Display for WithdrawError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            WithdrawError::InsufficientFunds {
                needed,
                available,
            } => {
                write!(
                    f,
                    "need {needed}, have {available}"
                )
            }
            WithdrawError::AccountFrozen => {
                write!(f, "account is frozen")
            }
            WithdrawError::InvalidAmount => {
                write!(f, "amount must be > 0")
            }
        }
    }
}

struct Account {
    balance: u32,
    frozen: bool,
}

impl Account {
    fn withdraw(
        &mut self,
        amount: u32,
    ) -> Result<u32, WithdrawError> {
        if self.frozen {
            return Err(WithdrawError::AccountFrozen);
        }
        if amount == 0 {
            return Err(WithdrawError::InvalidAmount);
        }
        if amount > self.balance {
            return Err(
                WithdrawError::InsufficientFunds {
                    needed: amount,
                    available: self.balance,
                },
            );
        }
        self.balance -= amount;
        Ok(self.balance)
    }
}

fn main() {
    let mut acc = Account { balance: 100, frozen: false };
    for amount in [30, 0, 500] {
        match acc.withdraw(amount) {
            Ok(left) => {
                println!("withdrew {amount}, {left} left")
            }
            Err(e) => {
                println!("withdraw {amount} failed: {e}")
            }
        }
    }
    acc.frozen = true;
    if let Err(e) = acc.withdraw(10) {
        println!("error: {e} ({e:?})");
    }
}
