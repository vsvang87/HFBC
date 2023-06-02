
function Main() {
  return (
    <ReactRouterDOM.BrowserRouter>
     
      <div className="navbar-container">
        <div className="center">
          <div className="navbar-links">
            <Navbar />

            <ReactRouterDOM.Route exact path="/">
                <Home />
            </ReactRouterDOM.Route>
            
            <ReactRouterDOM.Route exact path="/login">
             <Login />
              
            </ReactRouterDOM.Route>

            <ReactRouterDOM.Route exact path="/give">
               <Give />
            </ReactRouterDOM.Route>

            <ReactRouterDOM.Route exact path="/create_new_user">
              <CreateUser/>
            </ReactRouterDOM.Route>

          </div>
        </div>
        
      </div>
    </ReactRouterDOM.BrowserRouter>
  )
}
ReactDOM.render(<Main />, document.querySelector("#root"));