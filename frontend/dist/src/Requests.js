let link_to_backend = 'http://localhost:8000/queries/getData/?';


async function makeRequest() {
    let water = parseFloat(document.getElementById('inputWater').value);
    let chlorine = parseFloat(document.getElementById('inputChlorine').value);
    let potassium = parseFloat(document.getElementById('inputPotassium').value);
    let silicon = parseFloat(document.getElementById('inputSilicon').value);
    let iron = parseFloat(document.getElementById('inputIron').value);
    let sumOfAllElements = (water + chlorine + potassium + silicon + iron).toFixed(2);
    alert(sumOfAllElements)
    let link = link_to_backend + "water="+water+"&chlorine="+chlorine+"&pottasium="+potassium+"&silicon="+silicon+"&ferum="+iron;

    let getDataOptions = {
        method: 'get',
        url: link
    };

    if (parseInt(sumOfAllElements) === 1) {
        try {
            let response = await axios(getDataOptions);
            return response;
        }
        catch (e) {
            throw e;
        }
    } else {
        return null
    }

}
