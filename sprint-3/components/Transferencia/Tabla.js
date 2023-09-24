function Tabla({ datos }){
    const { id, nombre, fecha, monto } = datos

    return (
        <tbody>
            <tr>
                <td>{id}</td>
                <td>{nombre}</td>
                <td>{fecha}</td>
                <td>${Number(monto).toLocaleString('es-CO')}</td>
            </tr>
        </tbody>
    )
}

export default Tabla