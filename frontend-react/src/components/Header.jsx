import React, { useContext } from 'react'
import Button from './Button'
import { Link, useNavigate } from 'react-router-dom'
import { AuthContext } from '../AuthProvider'

const Header = () => {

  const {isLoggedIn , setisLoggedIn} = useContext(AuthContext)
  const navigate = useNavigate()

  const handleLogout = () => {
    localStorage.removeItem('accessToken')
    localStorage.removeItem('refreshToken')
    setisLoggedIn(false)
    navigate('/login')
  }
  return (
    <>
      <nav className='navbar container pt-4 pb-4 align-items-start'>

        <Link className='navbar-brand text-light' to="/">Stock Prediction Portal</Link>

        <div >
          {isLoggedIn ?  (
            <>
              <Button url='/dashboard' text='Dashboard' class='btn-outline-info' />
              &nbsp;
              <button   className='btn btn-danger' onClick={handleLogout}>logout</button>
            </>
          ) : (
            <>
              <Button text='Login' class='btn-outline-info' url='/login' />
              &nbsp;
              <Button text='Register' class='btn-info' url='/register' />
            </>
          )}
 
          
          

        </div>


      </nav>
    </>
  )
}

export default Header