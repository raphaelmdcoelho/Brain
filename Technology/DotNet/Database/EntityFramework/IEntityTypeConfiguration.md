```csharp
public class EntityConfiguration : IEntityTypeConfiguration<Entity>
{
	public void Configure(EntityTypeBuilder<Entity> builder)
	{
		builder.ToTable("name", DatabaseSchema.Name)
			HasKey(entity => entity.Id);
		
		builder.Property(entity => entity.Id)
			.HasColumnName("name")
			.HasColumnType("type");
			.IsRequired(true)
			.HasDefaultValue((T)default);

		builder.HasOne(entity => entity.parent)
			.WithMany(parent => parent.CollectionOfThis)
			.HasForeignKey(entity => entity.parentId);
	}
}
```

#dotnet #csharp 