const StarRating = ({ rating }) => {
  // Redondeamos hacia abajo para evitar medias estrellas
  const stars = [];

  for (let i = 1; i <= 5; i++) {
    stars.push(
      <i
        key={i}
        className={`bi bi-star-fill mx-1 ${i <= rating ? 'text-warning' : 'text-secondary'}`}
      ></i>
    );
  }

  return (
        <>
            {stars}
        </>
    );
};

export default StarRating;