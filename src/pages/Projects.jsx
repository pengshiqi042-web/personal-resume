import { useState } from 'react'
import { projects, categories } from '../data/projects'
import './Projects.css'

function Projects() {
  const [selectedCategory, setSelectedCategory] = useState('全部')
  const [selectedProject, setSelectedProject] = useState(null)

  const filteredProjects = selectedCategory === '全部'
    ? projects
    : projects.filter(project => project.category === selectedCategory)

  const openModal = (project) => {
    setSelectedProject(project)
  }

  const closeModal = () => {
    setSelectedProject(null)
  }

  return (
    <div className="projects-page">
      <div className="container">
        <div className="page-header">
          <h1 className="page-title">我的项目</h1>
          <p className="page-subtitle">探索我的作品和项目经验</p>
        </div>

        <div className="filter-tabs">
          {categories.map((category) => (
            <button
              key={category}
              className={`filter-tab ${selectedCategory === category ? 'active' : ''}`}
              onClick={() => setSelectedCategory(category)}
            >
              {category}
            </button>
          ))}
        </div>

        <div className="projects-grid">
          {filteredProjects.map((project) => (
            <div
              key={project.id}
              className="project-card"
              onClick={() => openModal(project)}
            >
              <div className="project-image">
                {project.image ? (
                  <img 
                    src={project.image} 
                    alt={project.title}
                    className="project-image-img"
                  />
                ) : (
                <div className="project-placeholder">
                  {project.title.charAt(0)}
                </div>
                )}
              </div>
              <div className="project-content">
                <span className="project-category">{project.category}</span>
                <h3 className="project-title">{project.title}</h3>
                <p className="project-description">{project.description}</p>
                <div className="project-tech">
                  {project.technologies.map((tech, idx) => (
                    <span key={idx} className="tech-tag">{tech}</span>
                  ))}
                </div>
                <button className="view-details-btn">查看详情 →</button>
              </div>
            </div>
          ))}
        </div>

        {filteredProjects.length === 0 && (
          <div className="no-projects">
            <p>该分类下暂无项目</p>
          </div>
        )}
      </div>

      {selectedProject && (
        <div className="modal-overlay" onClick={closeModal}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <button className="modal-close" onClick={closeModal}>×</button>
            <div className="modal-header">
              <span className="modal-category">{selectedProject.category}</span>
              <h2 className="modal-title">{selectedProject.title}</h2>
            </div>
            <div className="modal-body">
              <p className="modal-description">{selectedProject.details}</p>
              <div className="modal-section">
                <h3>主要功能</h3>
                <ul className="features-list">
                  {selectedProject.features.map((feature, idx) => (
                    <li key={idx}>{feature}</li>
                  ))}
                </ul>
              </div>
              <div className="modal-section">
                <h3>技术栈</h3>
                <div className="modal-tech">
                  {selectedProject.technologies.map((tech, idx) => (
                    <span key={idx} className="tech-tag">{tech}</span>
                  ))}
                </div>
              </div>
              
              {selectedProject.techDetails && (
                <div className="modal-section">
                  <h3>技术细节</h3>
                  <div className="tech-details">
                    {Object.entries(selectedProject.techDetails).map(([key, value], idx) => (
                      <div key={idx} className="tech-detail-item">
                        <span className="tech-detail-key">{key}:</span>
                        <span className="tech-detail-value">{value}</span>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {selectedProject.accomplishments && (
                <div className="modal-section">
                  <h3>项目亮点</h3>
                  <div className="project-accomplishments">
                    {Object.entries(selectedProject.accomplishments).map(([key, value], idx) => (
                      <div key={idx} className="accomplishment-item">
                        <span className="accomplishment-key">{key}:</span>
                        <span className="accomplishment-value">{value}</span>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {selectedProject.results && (
                <div className="modal-section">
                  <h3>项目成果</h3>
                  <div className="project-results">
                    {Object.entries(selectedProject.results).map(([key, value], idx) => (
                      <div key={idx} className="result-item">
                        <span className="result-key">{key}:</span>
                        <span className="result-value">{value}</span>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

export default Projects

