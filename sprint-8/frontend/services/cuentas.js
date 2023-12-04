import axios from 'axios'

const baseUrl = 'http://localhost:8000/cuenta/api'

const getAll = async (id) => {
    const response = await axios.get(`${baseUrl}/cuentas/${id}`);
    
    const cuentas = [response.data];

    const cuentasClasificadas = await Promise.all(cuentas.map(cuenta => clasificaCuentas(cuenta)))

    return cuentasClasificadas;
}

const clasificaCuentas = async (cuenta) => {
    try {
        const responseCC = await axios.get(`${baseUrl}/cuentas-corriente/${cuenta.account_id}`);
        
        let titleC;
        
        if (responseCC.data) {
            titleC = "Cuenta corriente"; 
        } else {
            // const responseCA = await axios.get(`${baseUrl}/cajas-ahorro/${cuenta.account_id}`);
            titleC = "Caja de ahorro"; 
        }
        
        const newCuenta = {
            ...cuenta,
            title: titleC
        };

        return newCuenta;
    } catch (error) {
        console.error("Error al clasificar cuenta:", error);
        throw error; // Puedes manejar el error según tus necesidades
    }
}

const create = async (newAccount) => {
    const response = await axios.post(baseUrl, newAccount)
    return response.data
}

const update = async (id, newAccount) => {
    const response = await axios.put(`${baseUrl}/${id}`, newAccount)
    return response.data
}

const remove = (id) => {
    return axios.delete(`${baseUrl}/${id}`)
}

const cuentaService = { getAll, create, update, remove }

export default cuentaService