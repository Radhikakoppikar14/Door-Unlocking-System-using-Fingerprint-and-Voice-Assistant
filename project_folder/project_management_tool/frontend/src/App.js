import React, { useState, useEffect } from 'react';

function TaskList({ projectId }) {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    fetch(`/projects/${projectId}/tasks`)
      .then(res => res.json())
      .then(data => setTasks(data.tasks));
  }, [projectId]);

  return (
    <ul>
      {tasks.map(task => (
        <li key={task.id}>{task.title} - {task.status}</li>
      ))}
    </ul>
  );
}

function ProjectList() {
  const [projects, setProjects] = useState([]);
  const [selectedProject, setSelectedProject] = useState(null);

  useEffect(() => {
    fetch('/projects')
      .then(res => res.json())
      .then(data => setProjects(data.projects));
  }, []);

  return (
    <div>
      <h1>Projects</h1>
      <ul>
        {projects.map(project => (
          <li key={project.id}>
            {project.name}
            <button onClick={() => setSelectedProject(project.id)}>
              Show Tasks
            </button>
            {selectedProject === project.id && <TaskList projectId={project.id} />}
          </li>
        ))}
      </ul>
    </div>
  );
}

function CreateProjectForm() {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('/projects', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name, description }),
    })
      .then(res => res.json())
      .then(data => {
        console.log(data.message);
        setName('');
        setDescription('');
      });
  };

  return (
    <div>
      <h2>Create a new project</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Project name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <input
          type="text"
          placeholder="Project description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
        <button type="submit">Create</button>
      </form>
    </div>
  );
}


function App() {
  return (
    <div>
      <CreateProjectForm />
      <ProjectList />
    </div>
  );
}

export default App;
