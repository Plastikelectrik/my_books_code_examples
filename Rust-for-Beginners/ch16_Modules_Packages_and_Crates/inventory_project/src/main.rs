mod inventory;

use inventory::Inventory;

fn main() {
    let mut inv = Inventory::new();
    inv.add("hammer", 3);
    inv.add("nails", 200);
    inv.add("hammer", 2);
    inv.print();
}
