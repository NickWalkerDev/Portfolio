function displayType(ingredient) {
    var ingredientType = ingredient.getAttribute("data-alcohol-ingredient");
    alert(ingredient.innerHTML + " is made from " + ingredientType );
}