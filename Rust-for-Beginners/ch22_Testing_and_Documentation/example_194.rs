// Book: Rust for Beginners — Example 194
pub fn shipping_cost(
    weight_kg: f64,
    express: bool,
) -> f64 {
    let base = if weight_kg <= 1.0 {
        4.0
    } else {
        4.0 + (weight_kg - 1.0) * 1.5
    };
    if express { base * 2.0 } else { base }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn light_package_costs_base_price() {
        assert_eq!(shipping_cost(0.5, false), 4.0);
    }

    #[test]
    fn heavy_package_costs_more() {
        assert_eq!(shipping_cost(3.0, false), 7.0);
    }

    #[test]
    fn express_doubles_the_price() {
        let normal = shipping_cost(3.0, false);
        let express = shipping_cost(3.0, true);
        assert_eq!(express, normal * 2.0);
    }
}
