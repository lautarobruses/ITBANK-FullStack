import styles from "@/styles/Inicio.module.css";

import React, { useState, useEffect } from 'react'

export default function Inicio() {
    const [tareas, setTareas] = useState([])

    useEffect(() => {
        fetch('https://jsonplaceholder.typicode.com/todos')
            .then(response => response.json())
            .then(data => {
                setTareas(data)
            }, 10)
            .catch(error => {
                console.error('Error: ', error)
            })
    }, [])

    return (
        <div className={`${styles.container}`}>
            <h1 className={`${styles.h1}`}>Tareas</h1>
            <ul className={`${styles.ul}`}>
                {tareas.map((tarea) => (
                    <li key="tarea.id" className={`${styles.li}`}>{tarea.title}</li>
                ))}
            </ul>
        </div>
    )
}