function Navbar() {
  return (
    <nav>
      <ReactRouterDOM.NavLink to="/">Home</ReactRouterDOM.NavLink>
      <ReactRouterDOM.NavLink to="/service">Service</ReactRouterDOM.NavLink>
      <ReactRouterDOM.NavLink to="/give">Give</ReactRouterDOM.NavLink>
      <ReactRouterDOM.NavLink to="/login">Log In</ReactRouterDOM.NavLink>
      <ReactRouterDOM.NavLink to="/create_new_user">Sign Up</ReactRouterDOM.NavLink>
    </nav>
  )
}

function Home() {
  return (
    <section>
      <div className="center">
        <h1>Home Page</h1>
      </div>
    </section>
  )
}

function Service() {
  return (
    <section>
      <div className="center">
        <div className="s-container">
          <h1>Service Page</h1>
        </div>
      </div>
    </section>
  )
}

function Give() {
  return (
    <div>
      <h1>Give to your local church</h1>
    </div>
  )
}
 
function Login() {
  const [email, setEmail] = React.useState("")
  const [password, setPassword] = React.useState("")
  return (
    <section>
      <div className="center">
        <div className="login-container">
          <h1>Login</h1>
          <form action="#" methods="Post">
            <label>Email:
              <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required/>
            </label>
            <label>Password:
              <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required/>
            </label>
            <button type="submit" className="login-btn">Login</button>
          </form>
       </div>
      </div>
    </section>
  )
}

function CreateUser() {
  return (
    <div>
      <h1>Create New User</h1>
    </div>
  )
}