import React, { useState, useEffect } from 'react'

export default function Home() {
    const [tareas, setTareas] = useState([])

    useEffect(() => {
        fetch('https://jsonplaceholder.typicode.com/todos')
            .then(response => response.json())
            .then(data => {
                setTareas(data)
            }, 10);
    }, [])

    return (
        <main>
            <ul>
                {tareas.map((tarea) => (
                    <li key="tarea.id">{tarea.title}</li>
                ))}
            </ul>
        </main>
    )
}