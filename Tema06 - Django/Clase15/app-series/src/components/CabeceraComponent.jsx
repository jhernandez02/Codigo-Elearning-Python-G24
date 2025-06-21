import { useContext } from "react";
import { Link, useNavigate } from "react-router-dom";
import { AppContext } from "../contexts/AppContext";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

function CabeceraComponent() {
  const navigate = useNavigate();
  const {usuario, logout} = useContext(AppContext);

  const handleLogout = () => {
    logout();
    navigate('/');
  };

  return (
    <>
    {usuario && (
      <Navbar expand="lg" className="bg-body-tertiary">
        <Container>
          <Navbar.Brand href="#home">SeriesApp</Navbar.Brand>
          <Navbar.Toggle />
          <Navbar.Collapse className="justify-content-end">
            <Nav className="me-auto">
                <li className="nav-item">
                    <Link to="/principal" className="nav-link">Inicio</Link>
                </li>
                <li className="nav-item">
                    <Link to="/favoritos" className="nav-link">Favoritos</Link>
                </li>
            </Nav>
            <Navbar.Text>
              <div className="me-3">
                <i className="bi bi-person-circle"></i> {usuario} | <a onClick={handleLogout} href="#" className="text-secondary">Salir</a>
              </div>
            </Navbar.Text>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    )}
    </>
  );
}

export default CabeceraComponent;