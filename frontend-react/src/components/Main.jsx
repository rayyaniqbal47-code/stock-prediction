import Button from './Button'
import Footer from './Footer'
import Header from './Header'

const Main = () => {
  return (
    <>
      
      <div className='container'>
        <div className='text-center p-5 bg-light-dark rounded'>

          <h1 className='text-light'>stock Prediction portal</h1>
          
          <p className='text-light lead'>Get real-time market forecasts powered by advanced AI analytics. Track trend shifts and predict stock movements with data-driven insights, helping you stay ahead of volatility. Make smarter investment decisions with our reliable daily predictive indicators</p>

          <Button text='login' class='btn-outline-info' />

        </div>
      </div>
    
    </>
  )
}

export default Main
