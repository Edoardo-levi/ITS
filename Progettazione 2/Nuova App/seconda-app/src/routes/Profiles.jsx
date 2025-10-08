import React from 'react'
import { Link, Outlet } from 'react-router-dom'

const Profiles = () => {
  return (
    <>
    <div>Profiles</div>
    <nav className='navbar'>
        <Link to="me"> My Profile</Link>
        <Link to="2"> Profile 2</Link>
    </nav>
    <div><Outlet></Outlet></div>
    </>
  )
}

export default Profiles