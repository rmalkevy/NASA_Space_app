function parseResponse(response) {
    let points = [];
    let data = response.data.mixed_values;
    let gradient = response.data.gradient;
    let length = data.length;

    let value = 0;
    for (let i = 0; i < length; i++) {
        if (data[i].value >= gradient.min && data[i].value <= gradient.averange) {
            value = data[i].value * 100;
        } else {
            value = data[i].value * 500;
        }
        points.push([parseFloat(data[i].latitude), parseFloat(data[i].longtitude), value.toString()]);
    }
    return { gradient: gradient, points: points};
}
