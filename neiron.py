import torch
import torch.nn as nn
import torch.optim as optim

# Создаем обучающие данные
data = torch.Tensor([[-1, -1], [-1, 1], [1, -1], [1, 1]])
labels = torch.Tensor([0, 1, 1, 0])

# Определяем нейронную сеть
class XORNet(nn.Module):
    def __init__(self):
        super(XORNet, self).__init__()
        self.hidden = nn.Linear(2, 2)  # Скрытый слой с двумя нейронами
        self.output = nn.Linear(2, 1)

    def forward(self, x):
        x = torch.relu(self.hidden(x))
        x = torch.sigmoid(self.output(x))
        return x

# Инициализируем сеть
net = XORNet()

# Определяем функцию потерь и оптимизатор
criterion = nn.BCELoss()  # Бинарная кросс-энтропия
optimizer = optim.SGD(net.parameters(), lr=0.001)

# Обучение сети
for epoch in range(40000):
    optimizer.zero_grad()
    output = net(data)
    loss = criterion(output, labels.view(-1, 1))
    loss.backward()
    optimizer.step()

# Проверяем результаты
with torch.no_grad():
    test_data = torch.Tensor([[-1, -1], [-1, 1], [1, -1], [1, 1]])
    predictions = net(test_data)
    print(predictions)
