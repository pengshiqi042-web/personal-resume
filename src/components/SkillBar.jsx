import './SkillBar.css'

function SkillBar({ name, proficiency }) {
  const getProficiencyClass = (proficiency) => {
    switch(proficiency) {
      case '精通':
        return 'proficiency-master'
      case '擅长':
        return 'proficiency-skilled'
      case '熟悉':
        return 'proficiency-familiar'
      default:
        return 'proficiency-familiar'
    }
  }

  return (
    <div className="skill-bar">
      <div className="skill-header">
        <span className="skill-name">{name}</span>
        <span className={`skill-proficiency ${getProficiencyClass(proficiency)}`}>
          {proficiency}
        </span>
      </div>
    </div>
  )
}

export default SkillBar




