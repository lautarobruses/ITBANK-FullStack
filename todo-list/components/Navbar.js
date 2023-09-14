import Link from 'next/link'

const NavBar = () => {
    return (
        <>
            <Link href={'/'}>Home</Link>
            <Link href={'/create'}>Create</Link>
        </>
    )
}

export default NavBar