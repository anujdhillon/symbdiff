import Header from './Components/Header';
import Footer from './Components/Footer';
import MainWindow from './Components/MainWindow';
import './App.scss';
import React from 'react';
function App() {
  return (
    <div className="App">
      <div className="header">
        <Header/>
      </div>
      <div  className="mainwindow">
          <MainWindow/>
      </div>
      <div className="footer">
        <Footer/>
      </div>

    </div>
  );
}

export default App;
