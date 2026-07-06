from training.trainer import Trainer

trainer = Trainer(

    dataset_path="datasets/processed/surface_d3_r3_p1e-03_100shots.npz",

    batch_size=16,

    epochs=20,

)

trainer.train()
