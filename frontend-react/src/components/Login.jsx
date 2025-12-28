import React, { useContext, useState } from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'
import { AuthContext } from '../AuthProvider'

const Login = () => {

  const [username , setUsername] = useState('')
  const [password , setPassword] = useState('')
  const [loading , setLoading] = useState(false)
  const [error , setError] = useState('')
  const navigate = useNavigate()
  const {isLoggedIn , setisLoggedIn} = useContext(AuthContext)

  const handleLogin = async (e) =>{
    e.preventDefault();
    setLoading(true)

    const userData = {
      username , password
    }

    try{
      const response = await axios.post("http://127.0.0.1:8000/api/v1/token/"  , userData)
      console.log(response.data)
      localStorage.setItem('accessToken' , response.data.access)
      localStorage.setItem('refreshToken' , response.data.refresh)
      setisLoggedIn(true)
      navigate('/dashboard')
    }catch(error){
      console.error('invalid credentials')
      setError('invalid credentials')
    }finally{
      setLoading(false)
    }
  }

  return (
    <>
      <div className='container'>
        <div className='row justify-content-center'>
          <div className='col-md-6 bg-light-dark p-5 rounded'>
            <h3 className='text-light text-center mb-4'>login to portal</h3>
            <form onSubmit={handleLogin}>
              <div className='mb-4'>
                <input type="text" className='form-control' placeholder='username' value={username} onChange={(e) => setUsername(e.target.value)}/>
              </div>

              <div className='mb-4'>
                <input type="password" className='form-control' placeholder='password' value={password} onChange={(e) => setPassword(e.target.value)}/>
              </div>

              {error && <div className='alert alert-danger'>{error}</div>}
              
              {loading ? (
                <button type="submit" className='btn btn-info d-block mx-auto ' disabled>logging in.....</button>
              ) : (
                <button type="submit" className='btn btn-info d-block mx-auto'>Login</button>
              )}
              
            </form>
          </div>
        </div>
      </div>
    </>
  )
}

export default Login
