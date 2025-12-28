import React , { useEffect } from 'react'
import axiosInstance from '../../axiosInstance'

const Dashboard = () => {

  useEffect(() => {
    const fetchProtectedData = async () => {
      try{
        const response = await axiosInstance.get("/ProtectedView")
        console.log(response.data)
      }catch(error){
        console.log('error fetching data:' , error)
      }
    }
    fetchProtectedData()
  } , [])

  return (
    <>
      
    </>
  )
}

export default Dashboard
