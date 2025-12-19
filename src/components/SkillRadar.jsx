import './SkillRadar.css'

function SkillRadar({ skills }) {
  const maxValue = 100
  const centerX = 150
  const centerY = 150
  const radius = 120
  const numSkills = skills.length
  const angleStep = (2 * Math.PI) / numSkills

  const getPoint = (index, value) => {
    const angle = index * angleStep - Math.PI / 2
    const distance = (value / maxValue) * radius
    const x = centerX + distance * Math.cos(angle)
    const y = centerY + distance * Math.sin(angle)
    return { x, y }
  }

  const points = skills.map((skill, index) => getPoint(index, skill.value))
  const pathData = points
    .map((point, index) => `${index === 0 ? 'M' : 'L'} ${point.x} ${point.y}`)
    .join(' ') + ' Z'

  return (
    <div className="skill-radar">
      <svg width="300" height="300" viewBox="0 0 300 300">
        {/* 背景网格 */}
        {[0.25, 0.5, 0.75, 1].map((scale) => (
          <circle
            key={scale}
            cx={centerX}
            cy={centerY}
            r={radius * scale}
            fill="none"
            stroke="var(--border-color)"
            strokeWidth="1"
            opacity={0.3}
          />
        ))}

        {/* 轴线 */}
        {skills.map((skill, index) => {
          const angle = index * angleStep - Math.PI / 2
          const x = centerX + radius * Math.cos(angle)
          const y = centerY + radius * Math.sin(angle)
          return (
            <line
              key={index}
              x1={centerX}
              y1={centerY}
              x2={x}
              y2={y}
              stroke="var(--border-color)"
              strokeWidth="1"
              opacity={0.3}
            />
          )
        })}

        {/* 技能区域 */}
        <path
          d={pathData}
          fill="var(--primary-color)"
          fillOpacity="0.2"
          stroke="var(--primary-color)"
          strokeWidth="2"
        />

        {/* 技能点 */}
        {points.map((point, index) => (
          <circle
            key={index}
            cx={point.x}
            cy={point.y}
            r="4"
            fill="var(--primary-color)"
          />
        ))}

        {/* 技能标签 */}
        {skills.map((skill, index) => {
          const angle = index * angleStep - Math.PI / 2
          const labelRadius = radius + 30
          const x = centerX + labelRadius * Math.cos(angle)
          const y = centerY + labelRadius * Math.sin(angle)
          return (
            <text
              key={index}
              x={x}
              y={y}
              textAnchor="middle"
              dominantBaseline="middle"
              fontSize="12"
              fill="var(--text-primary)"
              fontWeight="500"
            >
              {skill.name}
            </text>
          )
        })}
      </svg>
    </div>
  )
}

export default SkillRadar





