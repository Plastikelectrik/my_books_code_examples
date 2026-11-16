// Book: Rust for Beginners — Example 36
fn main() {
    let weight_kg: f64 = 72.0;
    let height_m: f64 = 1.78;

    let bmi = weight_kg / height_m.powi(2);

    let category = if bmi < 18.5 {
        "underweight"
    } else if bmi < 25.0 {
        "normal"
    } else if bmi < 30.0 {
        "overweight"
    } else {
        "obese"
    };

    let valid = weight_kg > 0.0 && height_m > 0.0;

    println!("Valid input: {valid}");
    println!("BMI: {bmi:.1}");
    println!("Category: {category}");
}
