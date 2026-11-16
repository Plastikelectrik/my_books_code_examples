use shipping::shipping_cost;

#[test]
fn a_typical_order_is_priced_correctly() {
    let parcels = [0.8, 2.0, 5.0];
    let total: f64 = parcels
        .iter()
        .map(|w| shipping_cost(*w, false))
        .sum();
    assert_eq!(total, 4.0 + 5.5 + 10.0);
}
