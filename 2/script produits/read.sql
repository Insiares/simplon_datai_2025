USE FoodDistribution;

-- SELECT * FROM principale;

select Code_article, Libelle, Cond, Famille, PU_HT from cond
left join principale on Cond.id = cond_id
left join famille on famille_id = famille.id
