import React from 'react'
import useSWR from 'swr'
export default function creat(){
    const { data,error } = useSWR('https://jsonplaceholder.typicode.com/todos', fetcher);
    if (error) {
         return <div>Error al cargarlos datos.</div>;} 
    if (!data) {
         return<div>Cargando datos...</div>;}
    function Cargar(){
     
    }
    import { useState } from 'react'

import { Form, Button } from 'react-bootstrap'

const NewBlogForm = ({ onCreate }) => {
    const [title, setTitle] = useState('')
    const [author, setAuthor] = useState('')
    const [url, setUrl] = useState('')

    const handleCreate = (event) => {
        event.preventDefault()
        onCreate({ title, author, url, likes: 0 })
        setAuthor('')
        setTitle('')
        setUrl('')
    }

    return (
        <>
            <h2>Create new</h2>
            <form onSubmit={handleCreate}>
                <Form.Group>
                    <Form.Label>title:</Form.Label>
                    <Form.Control
                        type='text'
                        name='title'
                        onChange={({ target }) => setTitle(target.value)}
                        placeholder="title of the blog"
                    />
                    <Form.Label>user:</Form.Label>
                    <Form.Control
                        type='text'
                        name='user'
                        onChange={({ target }) => setAuthor(target.value)}
                        placeholder="author of the blog"
                    />
                    <Form.Label>id:</Form.Label>
                    <Form.Control
                        type='text'
                        name='id'
                        onChange={({ target }) => setid(target.value)}
                        placeholder="id of the user"
                    />
                    <Button variant='outline-primary' type='submit'>
                        Create
                    </Button>
                </Form.Group>
            </form>
        </>
    )
}

export default NewBlogForm
    return (
        <div>
            <form onSubmit={Cargar()}>
                <label>

                    <input className='title' type="text" placeholder="Nombre de la tarea" />
                </label>
                <label>
                    <input ClassName='completed' type="bool" placeholder="Realizado" />
                </label>
                <button type='submit'>Cargar Informacíon</button>
            </form>
        </div>
    )
}
async function updateUser('https://jsonplaceholder.typicode.com/todos?', { title }: { arg: string }, {completed}:{arg: Bool}), {
    await fetch(url, {
      method: 'POST',
    })
  }