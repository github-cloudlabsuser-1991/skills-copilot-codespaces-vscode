// function to covert celsius
// to fahrenheit
function celsiusToFahrenheit(celsius) {
    return celsius * 9 / 5 + 32;
}

//function to convert fahrenheit
// to celsius
function fahrenheitToCelsius(fahrenheit) {
    return (fahrenheit - 32) * 5 / 9;
}

// driver code
let celsius = 100;
let fahrenheit = celsiusToFahrenheit(celsius);
console.log(celsius + "°C is " + celsiusToFahrenheit(celsius) + "°F");
console.log(fahrenheit + "°F is " + fahrenheitToCelsius(fahrenheit) + "°C");
