// App.jsx

import { useState, useContext } from 'react';
import { HashRouter as Router, Routes, Route } from "react-router-dom";
import CarModels from './pages/CarModels';
import AppContext from './context/AppContext';
import Navbar from './components/NavBar';


export default function App() {

  return (
    
      <Router>
        <div className='container'>
          <Navbar />
          {/* <LanguagePreference selectedLanguage={selectedLanguage} handleLanguageChange={handleLanguageChange}/> */}
        </div>
        <Routes>
            <Route path="/cars" element={<CarModels />} /> 
            
        </Routes>
      </Router>
      
  );
}