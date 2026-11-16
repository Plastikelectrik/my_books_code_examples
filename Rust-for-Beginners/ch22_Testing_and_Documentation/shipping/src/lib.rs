/// Calculates the shipping cost of a parcel in euros.
///
/// Parcels up to 1 kg cost a base price of 4.00 EUR.
/// Each additional kilogram costs 1.50 EUR.
/// Express delivery doubles the price.
///
/// # Examples
///
/// ```
/// use shipping::shipping_cost;
///
/// assert_eq!(shipping_cost(1.0, false), 4.0);
/// assert_eq!(shipping_cost(3.0, true), 14.0);
/// ```
///
/// # Panics
///
/// Panics if `weight_kg` is negative.
pub fn shipping_cost(
    weight_kg: f64,
    express: bool,
) -> f64 {
    assert!(
        weight_kg >= 0.0,
        "weight cannot be negative"
    );
    let base = if weight_kg <= 1.0 {
        4.0
    } else {
        4.0 + (weight_kg - 1.0) * 1.5
    };
    if express { base * 2.0 } else { base }
}
