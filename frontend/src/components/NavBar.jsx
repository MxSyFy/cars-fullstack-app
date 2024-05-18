// /components/NavBar.jsx

import {  Link } from "react-router-dom"

const Navbar = () =>{
  return (
  <>
    <ul className="navbar">
      <li className="items">
        <Link to="/cars">Cars</Link>
      </li>
    </ul>
  </>
  );
}
export default Navbar