import Contactos from '../components/Transferencia/contactos'

const Transferencia = () => {
    return(
        <div className="container">
            <div className="titulo">
                <h1>TRANSFERENCIAS</h1>
                <h3>TODOS LOS CONTACTOS</h3>
            </div>
            <div> {/*Contactos de las transferencias*/}
                <Contactos />
            </div>
        </div>
    )
}

export default Transferencia