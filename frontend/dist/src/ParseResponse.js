function parseResponse(response) {
    let points = [];
    let data = response.data.mixed_values;
    let gradient = response.data.gradient;
    let length = data.length;

    for (let i = 0; i < length; i++) {
        points.push([parseFloat(data[i].latitude), parseFloat(data[i].longtitude), data[i].value])
    }
    alert(points);
    return { gradient: gradient, points: points};
}
