import { Link, useLocation } from 'react-router-dom'
import './Navbar.css'

function Navbar() {
  const location = useLocation()

  const isActive = (path) => location.pathname === path

  return (
    <nav className="navbar">
      <div className="navbar-container">
        <Link to="/" className="navbar-logo">
          <span className="logo-text">个人简历</span>
        </Link>
        <ul className="navbar-menu">
          <li>
            <Link 
              to="/" 
              className={`navbar-link ${isActive('/') ? 'active' : ''}`}
            >
              首页
            </Link>
          </li>
          <li>
            <Link 
              to="/about" 
              className={`navbar-link ${isActive('/about') ? 'active' : ''}`}
            >
              关于我
            </Link>
          </li>
          <li>
            <Link 
              to="/projects" 
              className={`navbar-link ${isActive('/projects') ? 'active' : ''}`}
            >
              项目
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  )
}

export default Navbar

