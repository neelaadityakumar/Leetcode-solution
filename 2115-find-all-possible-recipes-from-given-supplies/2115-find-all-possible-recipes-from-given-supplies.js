var findAllRecipes = function(recipes, ingredients, supplies) {
    const availableSupplies = new Set(supplies);
    const dependency_Ing_ToReceipe = new Map();
    const indegree = new Array(recipes.length).fill(0);

    for (let i = 0; i < recipes.length; i++) {
        for (const ing of ingredients[i]) {
            if (!availableSupplies.has(ing)) {
                if (!dependency_Ing_ToReceipe.has(ing)) dependency_Ing_ToReceipe.set(ing, []);
                dependency_Ing_ToReceipe.get(ing).push([recipes[i],i]);
                indegree[i]++;
            }
        }
    }

    const queue = recipes.filter((_, i) => indegree[i] === 0);
    const result = [];
    while (queue.length > 0) {
        const currentRecipe = queue.shift();
        result.push(currentRecipe);
        const deps = dependency_Ing_ToReceipe.get(currentRecipe) || [];
        for (const dep of deps) {
            const depIdx = dep[1]
            indegree[depIdx]--;
            if (indegree[depIdx] === 0) queue.push(dep[0]);
        }
    }
    
    return result;
};
