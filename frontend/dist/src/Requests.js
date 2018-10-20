let link_to_backend = 'http://localhost:8000/queries/getData/?chlorine=0.2&water=0.4&pottasium=0.2&silicon=0.1&ferum=0.1';

let getDataOptions = {
    method: 'get',
    url: link_to_backend
};

async function makeRequest() {
    try {
        let response = await axios(getDataOptions);
        return response;
    }
    catch (e) {
        throw e;
    }
}
