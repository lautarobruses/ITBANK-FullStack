import {React, useState} from "react"

const Create = () => {

    const [user, setUser] = useState()
    const [id, setId] = useState()
    const [title, setTitle] = useState()
    const [completed, setCompleted] = useState()

    const Cargar = (e) => {
        e.prevenDefault()
        const listado = {
            user: user,
            id: id, 
            title: title,
            completed: completed,
        }
        setUser('')
        setId('')
        setTitle('')
        setCompleted('')
    }

    return(
        <div>
            <form onSubmit={Cargar()}>
                <label for='User'> Indicá tu usuario: </label>
                <input 
                    className="User" 
                    placeholder="Usuario"
                    onChange={setUser}
                />

                <label for = 'id'>Indicá tu ID: </label>
                <input 
                    className="id"
                    onChange={setId}
                />

                <label for='title'>Indicá el título de la tarea: </label>
                <input 
                    className="title" 
                    onChange={setTitle}
                />

                <button type='submit'>Cargar</button>
            </form>
        </div>
    )
}

export default Create()