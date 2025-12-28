import {useState , useContext, createContext} from 'react'

const AuthContext = createContext()


const AuthProvider = ({children}) => {

    const [isLoggedIn , setisLoggedIn] = useState(
        !!localStorage.getItem('accessToken')
    )

  return (
    <AuthContext.Provider value={{isLoggedIn , setisLoggedIn}}>
        {children}
    </AuthContext.Provider>
  )
}

export default AuthProvider
export {AuthContext}





