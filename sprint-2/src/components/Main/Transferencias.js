import React, { useState, useEffect } from 'react'
import styled from 'styled-components'

const bancos = ['Banco Nación', 'Banco Provincia', 'Banco Galicia', 'Banco Santander']

const FormularioStyled = styled.form`
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border: 1px solid #000;
    padding: 20px;
    width: 300px;
    margin: 0 auto;
`

const Transferencia = () => {
    const [opcion, setOpcion] = useState(null)
    const [datosPropia, setDatosPropia] = useState({
        cuentaOrigen: '',
        titular: '',
        importe: ''
    })
    const [datosTerceros, setDatosTerceros] = useState({
        cbuDestino: '',
        banco: '',
        titular: '',
        importe: ''
    })

    useEffect(() => {
        if (datosTerceros.cbuDestino.length === 21) {
            const bancoAleatorio = bancos[Math.floor(Math.random() * bancos.length)]
            setDatosTerceros(prevState => ({
                ...prevState,
                banco: bancoAleatorio
            }))
        }
    }, [datosTerceros.cbuDestino])

    const handleInputChangePropia = (event) => {
        setDatosPropia({
            ...datosPropia,
            [event.target.name] : event.target.value
        })
    }

    const handleInputChangeTerceros = (event) => {
        setDatosTerceros({
            ...datosTerceros,
            [event.target.name] : event.target.value
        })
    }

    const handleCuentaOrigenChange = (event) => {
        setDatosPropia({
            ...datosPropia,
            cuentaOrigen: event.target.value,
            cuentaDestino: event.target.value === 'cajaAhorro' ? 'cuentaCorriente' : 'cajaAhorro'
        })
    }

    const FormularioCuentaPropia = () => (
        <FormularioStyled>
            <label>Cuenta Origen</label>
            <select name="cuentaOrigen" onChange={handleCuentaOrigenChange}>
                <option value="cajaAhorro">Caja de Ahorro</option>
                <option value="cuentaCorriente">Cuenta Corriente</option>
            </select>
            <label>Titular</label>
            <input
                type="text"
                name="titular"
                onChange={handleInputChangePropia}
            />
            <label>Cuenta Destino ({datosPropia.cuentaOrigen === 'cajaAhorro' ? 'Cuenta Corriente' : 'Caja de Ahorro'})</label>
            <input
                type="text"
                name="cuentaDestino"
                value={datosPropia.cuentaOrigen === 'cajaAhorro' ? 'cuentaCorriente' : 'cajaAhorro'}
                readOnly
            />
            <label>Importe</label>
            <input
                type="text"
                name="importe"
                onChange={handleInputChangePropia}
            />
            <button type="submit">Enviar</button>
        </FormularioStyled>
    )

    const FormularioCuentaTerceros = () => (
        <FormularioStyled>
            <label>CBU Destino</label>
            <input
                type="text"
                name="cbuDestino"
                onChange={handleInputChangeTerceros}
            />
            {datosTerceros.cbuDestino.length !== 21 && (
                <p style={{ color: 'red' }}>El CBU debe tener 21 dígitos</p>
            )}
            {datosTerceros.cbuDestino.length === 21 && (
                <>
                    <label>Banco</label>
                    <input
                        type="text"
                        name="banco"
                        value={datosTerceros.banco}
                        readOnly
                    />
                </>
            )}
            <label>Titular</label>
            <input
                type="text"
                name="titular"
                onChange={handleInputChangeTerceros}
            />
            <label>Importe</label>
            <input
                type="text"
                name="importe"
                onChange={handleInputChangeTerceros}
            />
            <button type="submit">Enviar</button>
        </FormularioStyled>
    )

    return (
        <div>
            <button onClick={() => setOpcion('cuentaPropia')}>
                Transferir entre cuenta propia
            </button>
            {opcion === 'cuentaPropia' && <FormularioCuentaPropia />}
            <button onClick={() => setOpcion('cuentaTerceros')}>
                Transferir a una cuenta de terceros
            </button>
            {opcion === 'cuentaTerceros' && <FormularioCuentaTerceros />}
        </div>
    )
}

export default Transferencia
