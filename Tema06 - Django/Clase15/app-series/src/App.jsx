import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { AppProvider } from './contexts/AppContext';
import CabeceraComponent from './components/CabeceraComponent';
import LoginPage from './pages/LoginPage';
import PrincipalPage from './pages/PrincipalPage';
import SeriePage from './pages/SeriePage';
import './App.css';

function App() {
  return (
    <BrowserRouter>
      <AppProvider>
        <CabeceraComponent />
        <Routes>
          <Route path='/' element={<LoginPage />} />
          <Route path='/principal' element={<PrincipalPage />} />
          <Route path='/serie/:id' element={<SeriePage />} />
          <Route path='*' element={<h4 className='mt-3 text-center'>Error 404 - Página no encontrada</h4>} />
        </Routes>
      </AppProvider>
    </BrowserRouter>
  );
}

export default App;
